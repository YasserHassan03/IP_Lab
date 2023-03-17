from decimal import Decimal
import json
import boto3
#open smoothness_score.py file
with open("smoothness_score.json") as json_file:
    Drivers = json.load(json_file, parse_float=Decimal)
    #load data into dynamodb

def load_Drivers(Drivers, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')
    for Driver in Drivers:
        DriverId = int(['DriverId'])
        JourneyId = Driver['JourneyId']
        smoothness_score = Driver['smoothness_score'] # assuming smoothness_score is already included in the Driver dictionary
        ranking_list = []
        for i in range(1, len(ranking_list)):
            ranking_list.append(smoothness_score)
        ranking_list.sort(reverse=True)
        ranking = ranking_list.index(smoothness_score) + 1 
        print("Adding driver:", DriverId, JourneyId, "with ranking:", ranking)
        Driver['ranking'] = ranking
        table.put_item(Item=Driver)
if __name__ == '__main__':
    with open("Leaderboarddata.json") as json_file:
        Driver_list = json.load(json_file, parse_float=Decimal)
    load_Drivers(Driver_list)

    #shouldnt need ranking.py anymore