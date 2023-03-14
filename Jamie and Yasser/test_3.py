from flask import Flask,render_template
import boto3
import pandas as pd
from dynamodb_json import json_util as json


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
table = dynamodb.Table('Leaderboard')
    
    
response = table.scan()
data = response['Items']
    
    
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])
    
    

    
obj = pd.DataFrame(json.loads(data))

app = Flask(__name__)
@app.route('/')
def hello_world():
    return obj.to_html(header="true", table_id="table")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)