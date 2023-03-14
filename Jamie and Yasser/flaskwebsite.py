from flask import Flask,jsonify
import boto3
import pandas as pd
from dynamodb_json import json_util as json

app = Flask(__name__)


@app.route('/')
def hello():
 dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
 table = dynamodb.Table('Leaderboard')

 response = table.scan()
 data = response['Items']

 while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

 print("Driver: ")
 obj = pd.DataFrame(json.loads(data))
 df = [str(i) for i in obj.values]
    
 return (df)
