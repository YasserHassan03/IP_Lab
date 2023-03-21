import boto3
import matplotlib.pyplot as plt

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Leaderboard')

response = table.scan()
items = response['Items']

x_values = []
y_values = []

for item in items:
    x_values.append(item['x'])
    y_values.append(item['y'])

plt.plot(x_values, y_values)
plt.show()

