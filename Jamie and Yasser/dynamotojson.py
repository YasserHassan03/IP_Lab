import boto3
from boto3.dynamodb.conditions import Key, Key
import decimal
import json

AccessKey= "AKIASVJVETA6FMRSAQVW" #aws access keys
SecretKey = "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"
session = boto3.Session(
    aws_access_key_id=AccessKey,
    aws_secret_access_key=SecretKey,
    region_name="us-east-1"
)

dynamodb = session.resource('dynamodb')
valuesToSearch = ['sample data', 'sample data']
# paginator = dynamodb.get_paginator('scan')
table = dynamodb.Table('Leaderboard')
def getData(partitionKeyValue):
    data =[]
    response = table.query(
       KeyConditionExpression=Key("partitionKey").eq(partitionKeyValue) & Key('timestamp').between("2018-01-01 00:00:00","2024-01-31 00:00:00") #timestamp is sort key
    )
    data.extend(response['Items'])
  ##  while 'LastEvaluatedKey' in response:
    ##    response = table.query(
      ##      KeyConditionExpression=Key("partitionKey").eq(partitionKeyValue) & Key('timestamp').between("2018-01-01 00:00:00","2024-01-31 00:00:00")
        ##    ExclusiveStartKey=response['LastEvaluatedKey']
        ##x)
        
    data.extend(response['Items'])
    with open(f"folderName/{deviceId}.json","w+") as file1:
        file1.write(json.dumps(data))
        data = []

for i in valuesToSearch:
    getData(i)        
    print("Done for ",i)     