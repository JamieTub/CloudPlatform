import boto3
from botocore import endpoint

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName = 'Audio',
        KeySchema=[]
    )