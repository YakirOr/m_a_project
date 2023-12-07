FROM python:3.10

WORKDIR /scanner

COPY . /scanner/

RUN pip install --no-cache-dir boto3 \
    pip install dryable


CMD ["python3", "bin\bash"]
