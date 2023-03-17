import csv
import threading
import time
import boto3
from pprint import pprint
from botocore.exceptions import ClientError


def read_data(file_path):
    x_vals = []
    y_vals = []
    z_vals = []
    with open(file_path, "r") as file:
        for line in file:
            x_val, y_val, z_val = [float(val) for val in line.split(",")]
            x_vals.append(x_val)
            y_vals.append(y_val)
            z_vals.append(z_val)
    return x_vals, y_vals, z_vals
    
def smoothness_score(x_vals, y_vals, z_vals):
    x_jerk_list = []
    y_jerk_list = []
    z_jerk_list = []

    for i in range(1, len(x_vals)):
        x_jerk = (x_vals[i] - x_vals[i-1]) / 0.1 #replace 0.1 with their value
        y_jerk = (y_vals[i] - y_vals[i-1]) / 0.1
        z_jerk = (z_vals[i] - z_vals[i-1]) / 0.1
        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)

    x_jerk_magnitudes = [abs(x_jerk) for x_jerk in x_jerk_list]
    y_jerk_magnitudes = [abs(y_jerk) for y_jerk in y_jerk_list]
    z_jerk_magnitudes = [abs(z_jerk) for z_jerk in z_jerk_list]

    average_x_jerk_magnitude = sum(x_jerk_magnitudes) / len(x_jerk_magnitudes)
    average_y_jerk_magnitude = sum(y_jerk_magnitudes) / len(y_jerk_magnitudes)
    average_z_jerk_magnitude = sum(z_jerk_magnitudes) / len(z_jerk_magnitudes)

    x_smoothness_score = 1 / average_x_jerk_magnitude
    y_smoothness_score = 1 / average_y_jerk_magnitude
    z_smoothness_score = 1 / average_z_jerk_magnitude
    max_smoothness_score = 1 / 0.1  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride, #replace 0.1 with their value
    avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
    normalised_smoothness_score = avrg_smoothness / max_smoothness_score

    return normalised_smoothness_score


# Open the file for reading
i=0
with open("/home/ubuntu/Python Scripts and data for Lab 6/xyz.txt", "r") as file:
    contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
    x_vals = []
    y_vals = []
    z_vals = []
    for line in contents:
        values = line.strip().split(",")
        if len(values) != 3:  # skip lines that don't contain exactly 3 values
            continue
        try:
            x_vals.append(float(values[0]))
            y_vals.append(float(values[1]))
            z_vals.append(float(values[2]))
        except ValueError:  # skip lines that contain non-numeric data
            continue
    result = smoothness_score(x_vals, y_vals, z_vals)
    i= i +1

def put_leaderboard(DriverId,JourneyId, normalised_smoothness_score, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('Leaderboard')
        response = table.put_item(
           Item={
                'DriverId': DriverId,
                'JourneyId': JourneyId ,
                'info': {
                    'normalised_smoothness-score' : normalised_smoothness_score 
                }
            }
        )
    return DriverId, JourneyId, normalised_smoothness_score

#def put_leaderboard(DriverId,JourneyId, normalised_smoothness_score, dynamodb=None):
#
#    if not dynamodb:
#        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#        table = dynamodb.Table('DavidsResults')
#        response = table.put_item(
#           Item={
#                'DriverId': DriverId,
#                'JourneyId': JourneyId ,
#                'info': {
#                    'normalised_smoothness-score' : normalised_smoothness_score 
#                }
#            }
#        )
#    return DriverId, JourneyId, normalised_smoothness_score

def get_key(dynamodb=None):
    #dynamodb = boto3.client('dynamodb')

    # specify the table name and key value
    if not dynamodb:
        dynamodb = boto3.client('dynamodb', region_name='us-east-1')


    table_name = 'Leaderboard'
    partition_key_value = 'DriverId'
    sort_key_value = 'JourneyId'

    # create a dictionary containing the key values to retrieve
    key = {
        'partition-key-name': {'S': partition_key_value},
        'sort-key-name': {'S': sort_key_value}
    }

    # perform the query to retrieve the item
    response = dynamodb.get_item(TableName=table_name, Key=key)

    # extract the value for the sort key
    sort_key_value = response['Item']['sort-key-name']['S']

    return sort_key_value



if __name__ == '__main__':
    leaderboard_resp = put_leaderboard("David", get_key()+1, result)
    print("Put driver succeeded:")
    pprint(leaderboard_resp)









#def put_leaderboard(DriverId,JourneyId, normalied_smoothness_score, dynamodb=None):
#    if not dynamodb:
#        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#    smoothness_score()
#    table = dynamodb.Table('Leaderboard')
#    response = table.put_item(
#       Item={
#            'DriverId': DriverId,
#            'JourneyId': JourneyId,
#            'info': {
#                'normalised_smoothness_score' : normalised_smoothness_score
#            }
#        }
#    )
#    return response
#
#
#if __name__ == '__main__':
#    movie_resp = put_leaderboard("David", 12345, "7.56", "5.35")
#    print("Put driver succeeded:")
#    #pprint(leaderboard_resp)



#put normalised_smoothness_score into a json file
