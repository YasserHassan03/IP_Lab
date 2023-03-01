import json

data = [json.loads(line)
        for line in open('data.json', 'r', encoding='utf-8')]
print(data)

