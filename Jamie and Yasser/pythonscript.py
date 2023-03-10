from flask import Flask
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import boto3
from dynamodb_json import json_util as json
import pandas as pd
#import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')

def hello_world():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print("Driver: ")
   
    obj = pd.DataFrame(json.loads(data))

    return(obj)
    #if not dynamodb:
    #    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#
    #table = dynamodb.Table('Leaderboard')
#
    #try:
    #    response = table.get_item(Key={'DriverId': DriverId, 'JourneyId': JourneyId})
    #except ClientError as e:
    #    print(e.response['Error']['Message'])
    #else:
    #    return response['Item']


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

