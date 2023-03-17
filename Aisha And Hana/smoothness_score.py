#import csv
import threading 
from pprint import pprint
import boto3

  #csvreader = csv.reader(file, delimiter=',')
    
        
        #values = line.strip("[]")
        #values.split(",")
        #values = line[:-1]
        #values = values[:1]
        
        #x_val,y_val,z_val = (float(x) for x in line[1:-2].split(","))

def smoothness_score(x_val, y_val, z_val):

    threading.Timer(5.0, smoothness_score).start() #runs function every 5 second
    x_jerk_list = []
    y_jerk_list = []
    z_jerk_list = []
    
    for i in range(1, len(x_val)):
        x_jerk = (x_val[i] - x_val[i-1]) / 0.1 #replace 0.1 with their value
        y_jerk = (y_val[i] - y_val[i-1]) / 0.1
        z_jerk = (z_val[i] - z_val[i-1]) / 0.1
        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)
    for x_jerk in x_jerk_list:
        x_jerk_magnitude = abs(x_jerk)
        x_jerk_magnitudes = []
        x_jerk_magnitudes.append(x_jerk_magnitude)
    for y_jerk in y_jerk_list:
        y_jerk_magnitude = abs(y_jerk)
        y_jerk_magnitudes = []
        y_jerk_magnitudes.append(y_jerk_magnitude)
    for z_jerk in z_jerk_list:
        z_jerk_magnitude = abs(z_jerk)
        z_jerk_magnitudes = []
        z_jerk_magnitudes.append(z_jerk_magnitude)
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


    
def put_leaderboard(DriverId,JourneyId, normalised_smoothness_score, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('Leaderboard')
        response = table.put_item(
           Item={
                'DriverId': DriverId,
                'JourneyId': JourneyId,
                'info': {
                    'normalised_smoothness-score' : normalised_smoothness_score 
                }
            }
        )
    return DriverId, JourneyId, normalised_smoothness_score

if __name__ == '__main__':
    leaderboard_resp = put_leaderboard("david", "345678", result)
    print("Put driver succeeded:")









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
