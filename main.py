#James Lawn S1918451

import boto3
import createS3bucket
import createQueue


try:
    createS3bucket
    createQueue
except:
    print("Error in creation of services")
   

    



# #uploading of the audio file
# filename = 'audiofile.wav'
# bucket_name = 'MyBucketS1918451'
# s3.upload_file(filename, bucket_name, filename)

