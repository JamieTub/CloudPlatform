from os import walk
from re import T
import boto3
import logging
from botocore.exceptions import ClientError
import Queue
import time
import glob

s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')
sns = boto3.client('sns')

def fileUpload(bucketName, dir):

    try:
        for f in range(5):
            #give the file a file name for upload
            file_name = "Audio" + str(f + 1) + ".mp3"

            #split the uploads by 30 seconds
            if(f != 0):
                time.sleep(30)

            file = open(dir + file_name, 'rb')
            print(file)

            #upload the files to the bucket
            response = s3_client.put_object(
                Body=file,
                Bucket = bucketName,
                Key = file_name
            )

            print(file_name + " successfully uploaded.")
            if(response):
                Queue.sendSQSMessage(file_name)
            else:
                print("Error in file upload.")
                
        print("All files uploaded.")

    except ClientError as err:
        logging.error(err)
        return False

        