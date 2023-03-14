#def ranking(smoothness_score):
#
#	ranking_list = []
#
#	for i in range(1, len(ranking_list)):
#			ranking_list.append(smoothness_score)
#
#	ranking_list.sort(reverse=True)
#
#	for i in range(1, len(ranking_list)+1):
#            print(f"Rank {i}: {ranking_list[i-1]}")

#get rank of individual driver
def get_ranking(DriverId, JourneyId):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')
    response = table.query(
        KeyConditionExpression=Key('DriverId').eq(DriverId) & Key('JourneyId').eq(JourneyId)
    )
    if response['Items']:
        driver = response['Items'][0]
        ranking = driver['ranking']
        return ranking
    else:
        print("Driver not found in leaderboard.")
        return None
    
#update ranking of individual driver
def update_ranking(DriverId, JourneyId, smoothness_score):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Leaderboard')
    response = table.query(
		KeyConditionExpression=Key('DriverId').eq(DriverId) & Key('JourneyId').eq(JourneyId)
	)
    if response['Items']:
		driver = response['Items'][0]
    	ranking_list = []
    	for i in range(1, len(ranking_list)):
			ranking_list.append(smoothness_score)
			ranking_list.sort(reverse=True)
			ranking = ranking_list.index(smoothness_score) + 1
			driver['ranking'] = ranking
			table.put_item(Item=driver)
			return ranking
    else:
		print("Driver not found in leaderboard.")
		return None
    
#get ranking of all drivers
def get_all_rankings():
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('Leaderboard')
	response = table.scan()
	data = response['Items']
	while 'LastEvaluatedKey' in response:
		response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
		data.extend(response['Items'])
	for driver in items:
		DriverId = driver['DriverId']
		JourneyId = driver['JourneyId']
		ranking = driver['ranking']
		print(f"Driver {DriverId} ({JourneyId}): Rank {ranking}")
	