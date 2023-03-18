from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_movies(actor, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')
    print(f"Get year, title, genres, and lead actor")

    response = table.query(
        ProjectionExpression="#yr, title, genres, lead_actor",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=
            Key('lead_actor').eq(actor)
    )
    return response['Items']

if __name__ == '__main__':
    query_actor = 'Tom Hanks'
    print(f"Get movies from {query_actor}")
    movies = query_and_project_movies(query_actor)
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")