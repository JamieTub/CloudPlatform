import boto3
import logging
from botocore.exceptions import ClientError

def upload_file(file_name, bucket_name, object_name=None):
    file_name = 'Audio1.mp3'
    bucket_name = 'mybuckets1918451'
    
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
        print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def handler(event, context):
    sourceKey = event['Records'][0]['s3']['object']['key']
    print(sourceKey)