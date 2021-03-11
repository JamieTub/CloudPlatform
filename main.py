#James Lawn S1918451

import boto3
import createS3bucket


try:
    createS3bucket
except:
    print("Error in creation of services")
   

    # #creation of SQS queue
    # sqs = boto3.resource('sqs')

    # #create the queue
    # myQueue = sqs.create_queue(QueueName='MyQueueS1918451', Attributes={'DelaySeconds': '30'})



# #uploading of the audio file
# filename = 'audiofile.wav'
# bucket_name = 'MyBucketS1918451'
# s3.upload_file(filename, bucket_name, filename)

