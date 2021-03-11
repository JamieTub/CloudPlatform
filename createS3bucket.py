import boto3

try:
    #creation of the s3 client
    s3 = boto3.client('s3') 

    #creation of bucket
    myBucket = s3.create_bucket(Bucket='mybuckets1918451', CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'
})
except:
    print('client and bucket exist')