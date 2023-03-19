import csv
import threading
import time
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import decimal
import numpy as np

def delete_item(partition_key_value,sort_key_value):
    

    # Create an instance of the DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    # Define the table name and the key of the item to be deleted
    table_name = 'Leaderboard'
    key_to_delete = {'JourneyId': {'N': partition_key_value}, 'DriverId': {'S': sort_key_value}}

    # Delete the item from the table
    dynamodb.delete_item(
        TableName=table_name,
        Key=key_to_delete
    )   
    return ""

if __name__ == '__main__':
    delete_item("26", "Robert")