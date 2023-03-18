import boto3

def create_leaderboard_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='Leaderboard',
        KeySchema=[
        {
                'AttributeName': 'DriverId',    
                'KeyType': 'HASH'  # Sort key
            },
            {
                'AttributeName': 'JourneyId',
                'KeyType': 'RANGE'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'JourneyId',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'DriverId',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    dave_table = create_leaderboard_table()
    print("Table status:", dave_table.table_status)

