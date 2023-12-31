import time
from functions import revokerule
from functions import s3_upload
from get_values import *


s3 = session.client('s3')
ec2 = session.client('ec2')


#---file-name---
timestr = time.strftime("D%Y_%m_%d-T%H_%M_%S")
datelogfile = 'log-' + timestr +'.txt'
log_file_name=str('log.txt')


s3_bucket_name=S3_BUCKET_NAME

regions = [region['RegionName']
    for region in ec2.describe_regions()['Regions']]


anythingPrinted = False

print("Starting scanning")
response = ec2.describe_security_group_rules()
for region in regions:
 for rule in response['SecurityGroupRules']:
    try:
       if rule['IsEgress'] == False and rule['CidrIpv4'] == '0.0.0.0/0':
          with open(log_file_name, 'a+') as file:
           file.writelines('sg name:' + rule['GroupId'] +  ','+
                           ' ' + 'sgr_id: ' + rule['SecurityGroupRuleId'] +  
                           ' ' + 'from_cidr: ' + rule['CidrIpv4'] +  
                           ' ' + 'region: ' + region +  
                           ' ' + 'to_port: ' + str(rule['ToPort'])+ '\n')
                    
          anythingPrinted = True

          #---call to delete rule function---
          revokerule(rule['GroupId'], rule['SecurityGroupRuleId'])        
    except KeyError:
       print("Sorry, KeyError occurred for rule: " + rule['SecurityGroupRuleId'] )

if anythingPrinted:
    print("Uploading log file")
    #---change name and call the S3 function
    os.rename(log_file_name, datelogfile)
    s3_upload(datelogfile,s3_bucket_name)
else:
    print("There is no open inbound rules in the existing account")



