import os

# Get env variables
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
REGION = os.environ.get('REGION')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

print("Print secrets: " + AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)