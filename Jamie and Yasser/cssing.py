from flask import Flask, Markup
import boto3
import pandas as pd
from dynamodb_json import json_util as json
from flask import Response
from flask import Flask, Markup

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

    obj = pd.DataFrame(json.loads(data))
    df = [str(i) for i in obj.values]

    return (df)

# ...
@app.route('/')
def bob():
    # generate the HTML table string
    table_html = hello.to_html(header="true", table_id="table", classes="table table-striped table-hover", 
                               border="0", justify="center",
                               table_style='width:100%;max-width:700px', 
                               render_links=True,
                               attrs={"class": "pandas"})\
                    .replace('<table', '<table class="table"') \
                    .replace('<thead>', '<thead class="thead-light">') \
                    .replace('<table', '<table class="table"') \
                    .replace('<tbody>', '<tbody class="table-hover">') \
                    .replace('class="dataframe ', 'class="dataframe table-hover ')
                    
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
            }
        
            th {
                background-color: #f2f2f2 !important;
            }
        
            tr:hover {
                background-color: #f5f5f5 !important;
            }
        </style>
        '''
    
    return str(Markup(css + table_html))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
