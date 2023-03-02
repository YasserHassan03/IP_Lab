import boto3

def create_leaderboard_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='Leaderboard',
        KeySchema=[
            {
                'AttributeName': 'DriverId',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'JourneyId',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'DriverId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'JourneyId',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    movie_table = create_leaderboard_table()
    print("Table status:", leaderboard_table.table_status)

