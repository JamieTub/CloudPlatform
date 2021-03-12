#James Lawn S1918451

import boto3
import createS3bucket
import createQueue
import audioUpload


try:
    #creates and returns a bucket called 'myBucket'
    createS3bucket
    #creates and returns a queue called 'myQueue'
    createQueue
    print(createQueue.getQueueName)
    #add audio file upload to the returned queue
    #audioUpload.upload_file("","",None)
except:
    print("Error in creation of services")

