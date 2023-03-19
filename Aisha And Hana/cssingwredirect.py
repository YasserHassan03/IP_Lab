from flask import Flask, Markup
import boto3
import pandas as pd
from dynamodb_json import json_util as json
from flask import Response
from flask import Flask, Markup


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

app = Flask(__name__)
app.route('/')
@app.route('/')
def hello_world():
    html_table = get_item()
    return html_table
    
# ...
@app.route('/formatting')
def bob():
    # generate the HTML table string
    obj = hello_world()
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
    
    #<a href="{{http://ec2-3-90-81-83.compute-1.amazonaws.com:5000/formatting/David}}" >Login</a>

    table_html = f"<html><head><meta http-equiv='refresh' content='10'><title>Drivers Leaderboard</title></head><body><h1 style='text-align:center;'>Drivers Leaderboard</h1>{table_html}</body></html>"
    #hello=hello_world()
    return str(Markup(css + table_html))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)