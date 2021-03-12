import boto3
import logging
from botocore.exceptions import ClientError
import Queue

s3_client = boto3.client('s3')
sqs = boto3.client('sqs')
sns = boto3.client('sns')

def upload_file(file_name, bucket_name, object_name=None):
    print('audio called')
    file_name = 'Audio1.mp3'
    bucket_name = 'mybuckets1918451'
    queueUrl = Queue.getQueueUrl()
    print(queueUrl)
    
    if object_name is None:
        object_name = file_name

    # Upload the file  
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
        if response == True:
            sqsSendMessage = sqs.send_message(
                QueueUrl=queueUrl,
                DelaySeconds=10,
                MessageAttributes={
                    'Title': {
                    'DataType': 'String',
                    'StringValue': 'Audio Upload'
                    }
                },
                MessageBody=(
                'An audio file has been successfully uploaded.'
                )
            )
        else:
            print('error in sending success message')
    except ClientError as e:
        logging.error(e)
        return False
    return True

# def handler(event, context):
#     sourceKey = event['Records'][0]['s3']['object']['key']
#     print(sourceKey)