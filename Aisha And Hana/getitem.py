from flask import Flask, Markup
import boto3
import pandas as pd
from dynamodb_json import json_util as json
from flask import Response
from flask import Flask, Markup
from pprint import pprint
from boto3.dynamodb.conditions import Key



def get_leaderboard(DriverId,JourneyId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')

    try:
        response = table.get_item(Key={'DriverId': DriverId, 'JourneyId': JourneyId})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

def get_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items']) 

    obj = pd.DataFrame(json.loads(data))
    #obj = obj.sort_values(by=['smoothness'], ascending=False)
    return obj

if __name__ == '__main__':
    Leaderboard = get_leaderboard("David", 1)
    if Leaderboard:
        print("Get david succeeded:")
        pprint(Leaderboard)