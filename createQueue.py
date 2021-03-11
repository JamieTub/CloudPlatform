import boto3

try:
    #creation of SQS queue
    sqs = boto3.resource('sqs')

    #create the queue
    myQueue = sqs.create_queue(QueueName='MyQueueS1918451', Attributes={'DelaySeconds': '30'})

except:
    print('queue already exists')