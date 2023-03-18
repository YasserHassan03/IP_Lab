from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_leaderboard(DriverId,JourneyId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')

    try:
        response = table.get_item(Key={'DriverId': DriverId, 'JourneyId': JourneyId})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    Leaderboard = get_leaderboard("David","David" )
    if Leaderboard:
        print("Get david succeeded:")
        pprint(Leaderboard)