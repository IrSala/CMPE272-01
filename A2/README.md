# CMPE272-01-A1
Irwin Salamanca CMPE 272 Assignment 2

The purpose of this repository is to showcase the build of a servless web application with AWS Lambda and DynamoDB.


**Building the Serverless Web Application**
1. Create a table called StudentRecords with the partition key being student_id in DynamoDB through AWS Management Console.
   ![Alt text](screenshots/1.png)
   
2. Create an AWS Lambda Function in AWS Lambda through AWS Management Console and give Lambda function permission to be able to read/write to DynamoDB. ADD AND SPECIFY THE SECTION WHERE YOU CAN FIND THE SOURCE CODE!!!!! Below is a screenshot showing that the Lambda function was given permission to be able to read/wrte to DynamoDB.
   ![Alt text](screenshots/2.png)
   
3. Create an Rest API named StudentAPI in API Gateway through AWS Management Console. Setup POST and GET methods and then deploy the API.
   
   ![Alt text](screenshots/3.png)

_***Note**: Here is the invoke URL used to test the application: https://htgh6xl2aa.execute-api.us-east-2.amazonaws.com/tester*_

4. Create an API Gateway in API Gateway through AWS Management Console.


**Reflection**
I faced a couple challenges. 

From using AWS Lambda and DynamoDB I learned many things. I learned how to trigger a Lambda function using an API Gateway, interact with DynamoDB to perform basic CRUD operatinos, and how to deploy and test this application in the AWS environment. I also learned that both services are loosely coupled as they both function independently from each other while being able to communicate with each other. 

