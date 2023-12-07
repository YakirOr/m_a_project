# Exercise
## Project 1:
The goal of this workflow, its to find inbounds rules that open from 0.0.0.0/0, delete and will upload a log file to S3 Bucket with the information about the those rules.

the workflow will go through all the exicting secury groups in each VPC and will scan for those rules.  
In this repository, you will found 2 workflows.
- The first one - will create a Docker image with the scanner script and will push the image to Docker hub repository. 
    This workflow will be triggered by push to main/master

- The second workflow, will run a Docker container from the image we created, and will run the script. 
    This workflow will be triggered by scheduler (every day @ 8am)

## Project 2:
This is a clone and run project, this script will create a web app with the address http://localhost:3001/
for each request the response will be the punchline and the id fields from - : https://official-joke-
api.appspot.com/random_joke 


# prerequisites

For each project, there is a pre installation and some other configuration requirements:
## for project 1:
- Set AWS credentials and region and S3 Bucket (add it under secrets >> new repository secret):
    - For Access key: AWS_ACCESS_KEY_ID
    - For Secret key: AWS_SECRET_ACCESS_KEY
    - For region: REGION
    - For AWS S3 Bucket: S3_BUCKET_NAME
- For Docker Hub credentials:
    - For Username: DOCKERHUB_USERNAME
    - For Token: DOCKERHUB_TOKEN
> `PAY ATTENTION: This is a key sensitive, so the names must be the same as those here`


## for project 2:
For this web app, you need to run some installations before: 
```sh
install python
install flask
install jsonify
install requests
```
After the installations, run: 

```sh
cd web_app
python web_app.py
```




