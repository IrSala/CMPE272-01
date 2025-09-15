# CMPE272-01-A1
Irwin Salamanca CMPE 272 Assignment 2

The purpose of this repository is to showcase the build of a servless web application with AWS Lambda and DynamoDB that does CRUD operations (Create, Read, Update, Delete).


**Building the Serverless Web Application**
1. Create a table called StudentRecords with the partition key being student_id in DynamoDB through AWS Management Console.
   ![Alt text](screenshots/1.png)
   
2. Create an AWS Lambda Function in AWS Lambda through AWS Management Console and give Lambda function permission to be able to read/write to DynamoDB. The code used for the lambda function can be found [here](./lambda_function.py). The code is based on example code provided by the professor in the assignment word document. Below is a screenshot showing that the Lambda function was given permission to be able to read/wrte to DynamoDB.
   ![Alt text](screenshots/2.png)
   
3. Create an Rest API named StudentAPI in API Gateway through AWS Management Console. Setup POST and GET methods and then deploy the API.
   
   ![Alt text](screenshots/3.png)

_***Note**: Here is the invoke URL used to test the application: https://htgh6xl2aa.execute-api.us-east-2.amazonaws.com/tester*_


4. Test the application - mainly the create and read operations. Curl was used to test the API by sending HTTP requests to the deployed API Gateway. Below are the requests used to test the CREATE and READ operation.

curl -X POST \
  https://htgh6xl2aa.execute-api.us-east-2.amazonaws.com/tester/students \
  -H "Content-Type: application/json" \
  -d '{"student_id":"123","name":"John Doe","course":"Enterprise Software"}'


curl -X GET \
  "https://htgh6xl2aa.execute-api.us-east-2.amazonaws.com/tester/students?student_id=123"


Below is a screenshot of utilizing these two requests using curl and the results from using both. 

   ![Alt text](screenshots/4.png)

Below is a screenshot of added data points to the table in DynamoDB along with the original data point used to test the CREATE and READ operations.

   ![Alt text](screenshots/7.png)
   
**Optional**

The Lambda function was extended to be able to handle PUT and DELETE. A couple of lines of code were added to handle floating point numbers as a GPA category was added as a field. The DELETE and PUT meethods were added to the API.  
![Alt text](screenshots/5.png)

Below is a screenshot of testing all the methods - CREATE, READ, PUT, DELETE
![Alt text](screenshots/6.png)


**Reflection**

I faced a couple challenges. One of the challenges, which is expected, is navigating the AWS Console. It was hard to find things such as adding permisions to a Lambda function or finding the right applications to peform what is needed. One big challenge I faced was the code not working at all. I followed the guidelines in the word document verbatim and when it came time to test the CREATE and READ functions, the output was just "Hello form Lambda!" I thought i messed something up in the setup process so I redid everything and I stil had the same issue. Turns out I forgot to deploy the code in Lambda. After deploying the code everything worked as expected. 

From using AWS Lambda and DynamoDB I learned many things. I learned how to trigger a Lambda function using an API Gateway, interact with DynamoDB to perform basic CRUD operations, and how to deploy and test this application in the AWS environment. I also learned that both services are loosely coupled as they both function independently from each other while being able to communicate with each other. 

