#James Lawn S1918451

import boto3
import S3bucket
import Queue
import AudioUpload

try:
    #creates and returns a bucket called 'myBucket + studentId'
    S3bucket.createBucket()
    #creates and returns a queue called 'myQueue + studentId'
    Queue.createQueue()
    #add audio file upload to the returned queue
    AudioUpload.fileUpload(S3bucket.getBucketName(),"./res/")
except:
    print("Error in creation of services")

