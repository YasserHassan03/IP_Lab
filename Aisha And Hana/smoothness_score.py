import csv
import threading
import time
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import decimal 

def smoothness_score(x_vals, y_vals, z_vals):
    x_jerk_list = [1,1,1]
    y_jerk_list = [1,1,1]
    z_jerk_list = [1,1,1]
    x_jerk_magnitudes = [1,1,1]
    y_jerk_magnitudes = [1,1,1]
    z_jerk_magnitudes = [1,1,1]
    
    for i in range(1, len(x_vals)):
        x_jerk = decimal.Decimal((x_vals[i] - x_vals[i-1]) / (0.1))#replace 0.1 with their value
        y_jerk = decimal.Decimal((y_vals[i] - y_vals[i-1]) / 0.1)
        z_jerk = decimal.Decimal((z_vals[i] - z_vals[i-1]) / 0.1)

        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)
        
        x_jerk_magnitude = abs(round(x_jerk, 3))
        y_jerk_magnitude = abs(round(y_jerk, 3))
        z_jerk_magnitude = abs(round(z_jerk, 3))
        
        x_jerk_magnitudes.append(x_jerk_magnitude)
        y_jerk_magnitudes.append(y_jerk_magnitude)
        z_jerk_magnitudes.append(z_jerk_magnitude)
        
    average_x_jerk_magnitude = decimal.Decimal(sum(x_jerk_magnitudes) / len(x_jerk_magnitudes))
    average_y_jerk_magnitude = decimal.Decimal(sum(y_jerk_magnitudes) / len(y_jerk_magnitudes))
    average_z_jerk_magnitude = decimal.Decimal(sum(z_jerk_magnitudes) / len(z_jerk_magnitudes))
    
    x_smoothness_score = 1 / average_x_jerk_magnitude
    y_smoothness_score = 1 / average_y_jerk_magnitude
    z_smoothness_score = 1 / average_z_jerk_magnitude
    
    max_smoothness_score = 1 / 0.1  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride, #replace 0.1 with their value
    avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
    normalised_smoothness_score = avrg_smoothness
    
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
    return response['Items']

if __name__ == '__main__':
    with open("/home/ubuntu/Python Scripts and data for Lab 6/data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
        x_vals = [1]
        y_vals = [1]
        z_vals = [1]
        for line in contents:
            values = line.strip().split(",")
            while True:
                if len(values) != 3:  # skip lines that don't contain exactly 3 values
                    continue
                else:
                    for i in range(len(values)):
                        values[i] = int(values[i])
                        #values[i] = abs(values[i])
                try:
                    x_vals.append(values[0])
                    y_vals.append(values[1])
                    z_vals.append(values[2])
                except ValueError:  # skip lines that contain non-numeric data
                    continue
                result = decimal.Decimal((smoothness_score((x_vals), (y_vals), (z_vals))))
                query_driver ='David'
                leaderboard=query_and_project_drivers(query_driver)
                leaderboard_resp = put_leaderboard('David', leaderboard, result)
                #query_david = 'David'
                #david=query_david(query_david)
                #david_resp = put_david_leaderboard('David', david, result)
                print("Put driver succeeded:")