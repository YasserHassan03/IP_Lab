from pprint import pprint
import boto3

def put_leaderboard(DriverId,JourneyId, smoothness_score, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Davidsresults')
    response = table.put_item(
       Item={
            'DriverId': DriverId,
            'JourneyId': JourneyId,
            'info': {
                'smoothness-score' : smoothness_score
            }
        }
    )
    return DriverId, JourneyId, smoothness_score


if __name__ == '__main__':
    movie_resp = put_leaderboard("David", 1, 9876)
    print("Put driver succeeded:")
    #pprint(leaderboard_resp)