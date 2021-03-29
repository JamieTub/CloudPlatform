import boto3
import logging
from botocore import endpoint
from botocore.exceptions import ClientError

def create_table(name):
    #accessing the dynamoDB api here
    db = boto3.client('dynamodb')

    try:
        #creating the database table
        table = db.create_table(
            TableName = name,
            KeySchema = [
                {
                    'AttributeName': 'audioclipname',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'sentiment',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'audioclipname',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'sentiment',
                    'AttributeType': 'S'
                }
            ],
            Provisionedthroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        #allow time for the database table to be created
        table.meta.client.get_waiter('table_exists').wait(TableName=name)

        print(name + "was created.")
        return table

    except ClientError as error:
        logging.error(error)