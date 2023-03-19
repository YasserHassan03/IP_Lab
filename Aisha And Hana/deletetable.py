import boto3

def delete_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('DavidsResults')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("Movies table deleted.")