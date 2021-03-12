import boto3

def createBucket():
    try:
        #creation of the s3 client
        s3 = boto3.client('s3') 

        #creation of bucket
        myBucket = s3.create_bucket(Bucket='mybuckets1918451', CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'})
        print('bucket created')
        return myBucket
    except:
        print('bucket exists')