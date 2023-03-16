from flask import Flask, Markup
import boto3
import pandas as pd
from dynamodb_json import json_util as json
from flask import Response
from flask import Flask, Markup


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
table = dynamodb.Table('Leaderboard')
    
    
response = table.scan()
data = response['Items']
    
    
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items']) 

    
obj = pd.DataFrame(json.loads(data))
obj = obj.sort_values(by=['smoothness'], ascending=False)

app = Flask(__name__)
app.route('/')
def hello_world():
    return obj.to_html(header="true", table_id="table")

# ...
@app.route('/formatting')
def bob():
    # generate the HTML table string
    table_html = obj.to_html(header="true", table_id="table", classes="table table-striped table-hover", 
                               border="0", justify="center",
                               
                               render_links=True)
                     
                    
    css = '''
        <style>
            table {
                border-collapse: collapse !important;
                width: 100% !important;
                font-family: Arial, sans-serif !important;
                font-size: 14px !important;
                margin-bottom: 20px !important;
            }
        
            th, td {
                text-align: left !important;
                padding: 8px !important;
                border-bottom: 1px solid #ddd !important;
                background-color: #ffffff
            }
        
            th {
                background-color: #b56bdd !important;
            }
        
            tr:hover {
                background-color: #b56bdd !important;
            }
            body {
                background-color: #6bbfde;
            }
        </style>
        '''
    table_html = f"<html><head><meta http-equiv='refresh' content='30'><title>Drivers Leaderboard</title></head><body><h1 style='text-align:center;'>Drivers Leaderboard</h1>{table_html}</body></html>"
    return str(Markup(css + table_html))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

