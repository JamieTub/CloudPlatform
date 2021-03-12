#James Lawn S1918451

import boto3
import S3bucket
import Queue
import AudioUpload

try:
    #creates and returns a bucket called 'myBucket'
    S3bucket.createBucket()
    #creates and returns a queue called 'myQueue'
    Queue.createQueue()
    #add audio file upload to the returned queue
    AudioUpload.upload_file("","",None)
except:
    print("Error in creation of services")

    #6026

