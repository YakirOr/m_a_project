import os 
import boto3
# import sys
# import dryable


# dryable.set( '--dry-run' in sys.argv )

# Get env variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION = os.getenv('REGION')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

print(S3_BUCKET_NAME)


#build aws session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)