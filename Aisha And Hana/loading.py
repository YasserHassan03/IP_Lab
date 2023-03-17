import threading 
from pprint import pprint
import boto3

result = 2   
def put_leaderboard(DriverId,JourneyId, normalised_smoothness_score, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('Leaderboard')
        response = table.put_item(
           Item={
                'DriverId': DriverId,
                'JourneyId': JourneyId + 1,
                'info': {
                    'normalised_smoothness-score' : normalised_smoothness_score 
                }
            }
        )
    return DriverId, JourneyId, normalised_smoothness_score

if __name__ == '__main__':
    journey= str(JourneyId + 1)
    leaderboard_resp = put_leaderboard("David", journey , result)
    print("Put driver succeeded:")
    pprint(leaderboard_resp)
