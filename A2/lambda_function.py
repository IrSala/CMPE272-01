import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def _json_default(o):
    if isinstance(o, Decimal):
        return float(o)
    raise TypeError

def lambda_handler(event, context):
    method = event.get('httpMethod')

    if method == 'POST':
        if not event.get('body'):
            return {'statusCode': 400, 'body': json.dumps('Missing request body')}
        student = json.loads(event['body'], parse_float=Decimal)
        if 'student_id' not in student:
            return {'statusCode': 400, 'body': json.dumps('student_id is required')}
        table.put_item(Item=student)
        return {'statusCode': 200, 'body': json.dumps('Student record added successfully')}

    elif method == 'GET':
        qs = event.get('queryStringParameters') or {}
        student_id = qs.get('student_id')
        if not student_id:
            return {'statusCode': 400, 'body': json.dumps('student_id query parameter is required')}
        response = table.get_item(Key={'student_id': student_id})
        item = response.get('Item')
        if not item:
            return {'statusCode': 404, 'body': json.dumps('Student not found')}
        return {'statusCode': 200, 'body': json.dumps(item, default=_json_default)}

    elif method == 'PUT':
        if not event.get('body'):
            return {'statusCode': 400, 'body': json.dumps('Missing request body')}
        data = json.loads(event['body'], parse_float=Decimal)
        student_id = data.get('student_id')
        if not student_id:
            return {'statusCode': 400, 'body': json.dumps('student_id is required')}

        update_keys = [k for k in data.keys() if k != 'student_id']
        if not update_keys:
            return {'statusCode': 400, 'body': json.dumps('No fields to update')}

        update_expr = "SET " + ", ".join(f"#{k} = :{k}" for k in update_keys)
        expr_names = {f"#{k}": k for k in update_keys}
        expr_vals = {f":{k}": data[k] for k in update_keys}

        try:
            result = table.update_item(
                Key={'student_id': student_id},
                UpdateExpression=update_expr,
                ExpressionAttributeNames=expr_names,
                ExpressionAttributeValues=expr_vals,
                ConditionExpression="attribute_exists(student_id)",  #fail if record doesn’t exist
                ReturnValues='ALL_NEW'
            )
        except table.meta.client.exceptions.ConditionalCheckFailedException:
            return {'statusCode': 404, 'body': json.dumps('Student not found')}

        return {'statusCode': 200, 'body': json.dumps(result.get('Attributes', {}), default=_json_default)}

    elif method == 'DELETE':
        qs = event.get('queryStringParameters') or {}
        student_id = qs.get('student_id')
        if not student_id:
            return {'statusCode': 400, 'body': json.dumps('student_id query parameter is required')}
        try:
            table.delete_item(
                Key={'student_id': student_id},
                ConditionExpression="attribute_exists(student_id)"  #fail if not found
            )
        except table.meta.client.exceptions.ConditionalCheckFailedException:
            return {'statusCode': 404, 'body': json.dumps('Student not found')}
        return {'statusCode': 200, 'body': json.dumps('Student record deleted successfully')}

    else:
        return {'statusCode': 405, 'body': json.dumps(f'Method {method} not allowed')}