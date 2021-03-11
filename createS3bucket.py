import boto3

#creation of the s3 client
s3 = boto3.client('s3') 

#creation of bucket
s3.create_bucket(Bucket='MyBucketS1918451')