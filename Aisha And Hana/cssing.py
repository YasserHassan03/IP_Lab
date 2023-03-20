from flask import Flask, Markup
import boto3
import pandas as pd
from dynamodb_json import json_util as json
from flask import Response
from flask import Flask, Markup
from pprint import pprint
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


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
    
    
    table_html = ftable_html = f"<html><head><meta http-equiv='refresh' content='10'><title>Drivers Leaderboard</title></head><body><h1 style='text-align:center;'>Drivers Leaderboard</h1>{table_html}<p align=\"center\"><a href=formatting/David ><button class=grey style=\"height:75px;width:150px\">David's Resutls</button></a></p><p align=\"center\"><a href=formatting/Robert ><button class=grey style=\"height:75px;width:150px\">Robert's Resutls</button></a></p></body></html>"

    return str(Markup(css + table_html))


#def query_and_project_movies(DriverId, dynamodb=None):
  #  if DriverId == 'Robert':
   #     DriverId = 'Robert'

#    if not dynamodb:
 #       dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    #table = dynamodb.Table(DriverId+'sresults')

#    print(f"Get year, title, genres, and lead actor")
   # if DriverId == 'David':
    #    DriverId = 'David'
    #table = dynamodb.Table(DriverId+'sresults')
    #response = table.query(
     #   ProjectionExpression="#DriverId, JourneyId, smoothness_score",
       # ExpressionAttributeNames={"#DriverId": DriverId},
        #KeyConditionExpression=
         #   Key('DriverId').eq(DriverId)
    #)
    #data = response['Items']
    #bj = pd.DataFrame(json.loads(data))
    #obj = obj.sort_values(by=['smoothness'], ascending=False)
    #return obj

def query_david():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Davidsresults')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items']) 

    obj = pd.DataFrame(json.loads(data))
    #obj = obj.sort_values(by=['smoothness'], ascending=False)
    return obj

def query_robert():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Robsresults')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items']) 

    obj = pd.DataFrame(json.loads(data))
    #obj = obj.sort_values(by=['smoothness'], ascending=False)
    return obj


@app.route('/formatting/David')
def Fred():
    # generate the HTML table string
    obj = query_david()
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
    
    
    table_html = ftable_html = f"<html><head><meta http-equiv='refresh' content='10'><title>David's Results</title></head><body><h1 style='text-align:center;'>David's result</h1>{table_html}<p align=\"center\"></p></html>"

    return str(Markup(css + table_html))

@app.route('/formatting/Robert')
def dave():
    # generate the HTML table string
    obj = query_robert()
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
    
    
    table_html = ftable_html = f"<html><head><meta http-equiv='refresh' content='10'><title>Rob's Leaderboard</title></head><body><h1 style='text-align:center;'>Rob's Leaderboard</h1>{table_html}<p align=\"center\"></p></html>"
    #<a href=formatting/David ><button class=grey style=\"height:75px;width:150px\">David's Resutls</button></a></p><p align=\"center\"><a href=formatting/Robert ><button class=grey style=\"height:75px;width:150px\">Robert's Resutls</button></a></p></body></html>"

    return str(Markup(css + table_html))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

