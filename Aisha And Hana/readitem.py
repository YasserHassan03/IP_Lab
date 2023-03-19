from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key


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

def extract_journey_id(response_dict):
    try:
        journey_id = response_dict['Items'][0]['JourneyId']
    except (IndexError, KeyError):
        journey_id = None
    return journey_id

def query_and_project_drivers(DriverId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Leaderboard')
    print(f"Get driver, journeyid, and smoothnessscore")

    response = table.query(
        ProjectionExpression="#JourneyId, DriverID,smoothness_score",
        ExpressionAttributeNames={"#JourneyId": "JourneyId"},
        KeyConditionExpression=
            Key('DriverId').eq(DriverId)
    )
    return response
if __name__ == '__main__':
    query_driver ='Robert'
    test=query_and_project_drivers(query_driver)
    #print(test)
    leaderboard = extract_journey_id(test)
    leaderboard_resp = get_leaderboard('Robert', leaderboard)
    print(leaderboard_resp)
