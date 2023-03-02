from decimal import Decimal
import json
import boto3
def load_Drivers(Drivers, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')
    for Driver in Drivers:
        DriverId = int(['DriverId'])
        JourneyId = Driver['JourneyId']
        print("Adding driver:", DriverId, JourneyId)
        table.put_item(Item=Driver)
if __name__ == '__main__':
    with open("Leaderboarddata.json") as json_file:
        Driver_list = json.load(json_file, parse_float=Decimal)
    load_Drivers(Driver_list)