from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_movies(DriverId, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Davidsresults')
    print(f"Get year, title, genres, and lead actor")

    response = table.query(
        ProjectionExpression="#DriverId, JourneyId, smoothness_score",
        ExpressionAttributeNames={"#DriverId": "DriverId"},
        KeyConditionExpression=
            Key('DriverId').eq(DriverId)
    )
    return response['Items']

if __name__ == '__main__':
    query_actor = 'David'
    print(f"Get movies from {query_actor}")
    movies = query_and_project_movies(query_actor)
    print(movies)
    #for movie in movies:
    #    print(f"\n{movie['DriverId']} : {movie['DriverId']}")