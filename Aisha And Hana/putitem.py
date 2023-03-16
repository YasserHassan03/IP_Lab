from pprint import pprint
import boto3

def put_leaderboard(DriverId,JourneyId, smoothness, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')
    response = table.put_item(
       Item={
            'DriverId': DriverId,
            'JourneyId': JourneyId,
            'info': {
                'smoothness' : smoothness
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_leaderboard("David", 12345, "7.56", "5.35")
    print("Put driver succeeded:")
    #pprint(leaderboard_resp)