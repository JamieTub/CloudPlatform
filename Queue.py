import boto3

myQueue = None
queueUrl = 'https://sqs.eu-west-2.amazonaws.com/018608591185/MyQueueS1918451'

def createQueue():
    try:
        #creation of SQS queue
        sqs = boto3.resource('sqs')

        #create the queue
        myQueue = sqs.create_queue(QueueName='MyQueueS1918451')
        print('queue created')

    except:
        print('queue already exists')

def getQueueUrl():
    print('called get queue url')
    try:
        sqs = boto3.client('sqs')
        #get the name of the queue
        myQueue = sqs.get_queue_url(QueueName='MyQueueS1918451')
        return myQueue['QueueUrl']
    except:
        print('Error attaining Queue')

def sendSQSMessage(fileName):
    sqs = boto3.client('sqs')
    queueUrl = getQueueUrl()
    print(queueUrl)

    sqs.send_message(
        QueueUrl = queueUrl,
        MessageAttributes = {
            'FileName': {
                'DataType': 'String',
                'StringValue': fileName
            }
        },
        MessageBody = (
            fileName
        )
    )

    print('SQS Message Sent.')