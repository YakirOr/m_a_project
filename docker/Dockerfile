FROM python:3.10

# ARG AWS_ACCESS_KEY_ID
# ARG AWS_SECRET_ACCESS_KEY
# ARG REGION
# ARG S3_BUCKET_NAME


ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV REGION=$REGION
ENV S3_BUCKET_NAME=$S3_BUCKET_NAME


WORKDIR /scanner

COPY . /scanner/

RUN pip install --no-cache-dir boto3 
    # pip install dryable
RUN apt-get update && apt-get install -y expect



CMD ["unbuffer", "python", "-u", "scanner/get_values.py"]
