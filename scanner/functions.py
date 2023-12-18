# import os
# import boto3
from get_values import *
from botocore.exceptions import ClientError


s3 = session.client('s3')
client = session.client('ec2')

# @dryable.Dryable()
def revokerule(Group_Id, sgr_Id):
 if not args:
    try:
     delete= client.revoke_security_group_ingress(
        GroupId=Group_Id,
        SecurityGroupRuleIds=[sgr_Id])
     
    except ClientError:
        print("Sorry, ingress security group rule can not be deleted.")
        raise
    else:
        print("The ingress rule successfully deleted")
 else:
    print("This is dry run mode")



def s3_upload(file_name , bucket_name):
      s3.upload_file(file_name, bucket_name, file_name)
      print("The file was successfully uploaded ")
      

