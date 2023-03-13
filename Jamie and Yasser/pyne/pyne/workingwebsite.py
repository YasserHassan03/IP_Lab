from flask import Flask,jsonify
import boto3
app = Flask(__name__)


@app.route('/')
def hello():
    db = boto3.resource('dynamodb','us-east-1')
    tab = db.Table('Leaderboard')
    i = tab.scan()["Items"][0]
    return jsonify(i)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)