FROM python:3.10

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV REGION=$REGION
ENV S3_BUCKET_NAME=$S3_BUCKET_NAME


WORKDIR /scanner

COPY . /scanner/

RUN pip install --no-cache-dir boto3 

ENTRYPOINT  ["python","scanner/in_scanner.py"]

# CMD [ "--dry-run"]