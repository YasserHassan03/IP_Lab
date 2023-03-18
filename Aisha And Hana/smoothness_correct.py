import csv
import threading
import time
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import decimal
import numpy as np

def smoothness_score(x_vals, y_vals, z_vals, time_interval):
    x_jerk_list = [1,1,1]
    y_jerk_list = [1,1,1]
    z_jerk_list = [1,1,1]
    x_jerk_magnitudes = [1,1,1]
    y_jerk_magnitudes = [1,1,1]
    z_jerk_magnitudes = [1,1,1]
    x_smoothness_scores = []
    y_smoothness_scores = []
    z_smoothness_scores = []
    
    for i in range(1, len(x_vals)):
        x_jerk = decimal.Decimal((x_vals[i] - x_vals[i-1]) / time_interval)
        y_jerk = decimal.Decimal((y_vals[i] - y_vals[i-1]) / time_interval)
        z_jerk = decimal.Decimal((z_vals[i] - z_vals[i-1]) / time_interval)
        
        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)
        
        x_jerk_magnitude = abs(decimal.Decimal(x_jerk))
        y_jerk_magnitude = abs(decimal.Decimal(y_jerk))
        z_jerk_magnitude = abs(decimal.Decimal(z_jerk))
        
        x_jerk_magnitudes.append(x_jerk_magnitude)
        y_jerk_magnitudes.append(y_jerk_magnitude)
        z_jerk_magnitudes.append(z_jerk_magnitude)

        window_size = 5

        for i in range(len(x_jerk_magnitudes)):
            start = max(0, i-window_size)
            end = min(len(x_jerk_magnitudes), i+window_size)
            x_jerk_window = x_jerk_magnitudes[start:end]
            y_jerk_window = y_jerk_magnitudes[start:end]
            z_jerk_window = z_jerk_magnitudes[start:end]
            
            x_smoothness_score = 1 / decimal.Decimal(np.mean(x_jerk_window))
            y_smoothness_score = 1 / decimal.Decimal(np.mean(y_jerk_window))
            z_smoothness_score = 1 / decimal.Decimal(np.mean(z_jerk_window))

            x_smoothness_scores.append(x_smoothness_score)
            y_smoothness_scores.append(y_smoothness_score)
            z_smoothness_scores.append(z_smoothness_score)
        
        
    average_x_smoothness = decimal.Decimal(np.mean(x_smoothness_scores))
    average_y_smoothness = decimal.Decimal(np.mean(y_smoothness_scores))
    average_z_smoothness = decimal.Decimal(np.mean(z_smoothness_scores))
    
    x_smoothness_score = 1 / average_x_smoothness
    y_smoothness_score = 1 / average_y_smoothness
    z_smoothness_score = 1 / average_z_smoothness
    
    max_smoothness_score = 1 / decimal.Decimal(0.1)  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride
    avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
    normalised_smoothness_score = avrg_smoothness / max_smoothness_score
    
    return decimal.Decimal(normalised_smoothness_score)

def put_leaderboard(DriverId, JourneyId, smoothness_score, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')
    response = table.put_item(
        Item={
            'DriverId': DriverId,
            'JourneyId': JourneyId,
            'info': {
                'smoothness_score': smoothness_score
            }
        }
    )
    return DriverId, JourneyId, smoothness_score



def query_and_project_drivers(DriverId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')
    print(f"Get year, title, genres, and lead actor")

    response = table.query(
        ProjectionExpression="#JourneyId, DriverID,smoothness_score",
        ExpressionAttributeNames={"#JourneyId": "JourneyId"},
        KeyConditionExpression=
            Key('DriverId').eq(DriverId)
    )
    return response

def extract_journey_id(response_dict):
    journey_id = response_dict['Items'][0]['JourneyId']
    return int(journey_id)



def process_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
        x_vals = [1]
        y_vals = [1]
        z_vals = [1]
        for line in contents:
            values = line.strip().split(",")
            if len(values) != 3:  # skip lines that don't contain exactly 3 values
                continue
            try:
                x_vals.append(int(values[0]))
                y_vals.append(int(values[1]))
                z_vals.append(int(values[2]))
            except ValueError:  # skip lines that contain non-numeric data
                continue
    return x_vals, y_vals, z_vals

if __name__ == '__main__':
    x_vals, y_vals, z_vals = process_file("/home/ubuntu/Python Scripts and data for Lab 6/data.txt")
    result = decimal.Decimal((smoothness_score(x_vals, y_vals, z_vals, 1.0)))
    query_driver ='David'
    test=query_and_project_drivers(query_driver)
    leaderboard = extract_journey_id(test)

    leaderboard_resp = put_leaderboard('David', leaderboard, result)
    #print(leaderboard)
    #print(result)
    #query_david = 'David'
    #david=query_david(query_david)
    #david_resp = put_david_leaderboard('David', david, result)
    print("Put driver succeeded:")