
import pyotp
import boto3
import os
import json
import sys
import getopt
import configparser

arguments = len(sys.argv) - 1
if arguments != 1:
    print ('aws-creds <stage>')
    sys.exit(2)

stage = sys.argv[1]

config = configparser.ConfigParser()
config.read('/home/ec2-user/.aws/config')
try:
    config_info = config["profile {}".format(stage)]
except:
    print('Could not find a profile for {} in ~/aws.config'.format(stage))
    sys.exit(2)


if os.path.exists("/home/ec2-user/.aws/credentials"):
    os.remove("/home/ec2-user/.aws/credentials")
config.read('/home/ec2-user/.aws/credentials_file')
keys = config['default']
key = keys['aws_access_key_id']
secret = keys['aws_secret_access_key']


with open('/home/ec2-user/.aws/otp', 'r') as file:
    MFA = file.read().strip()




role_arn = config_info['role_arn']
serial_number = config_info['mfa_serial']

sts_client = boto3.client('sts', aws_access_key_id=key,aws_secret_access_key=secret)
totp = pyotp.TOTP(MFA)
token = totp.now()


assumed_role_object=sts_client.assume_role(
    DurationSeconds=3600,
    RoleSessionName="AssumeRoleSession1",
    SerialNumber=serial_number,
    TokenCode=token,
    RoleArn=role_arn
)

creds = {
    "AWS_ACCESS_KEY_ID_TEMP" :assumed_role_object['Credentials']['AccessKeyId'],
    "AWS_SECRET_ACCESS_KEY_TEMP": assumed_role_object['Credentials']['SecretAccessKey'],
    "AWS_SESSION_TOKEN" : assumed_role_object['Credentials']['SessionToken']
}

f = open("/home/ec2-user/.aws/credentials","w")
content = """
[default]
aws_access_key_id={}
aws_secret_access_key={}
aws_session_token={}
""".format(assumed_role_object['Credentials']['AccessKeyId'],assumed_role_object['Credentials']['SecretAccessKey'],assumed_role_object['Credentials']['SessionToken'])

f.write(content)
f.close()
print("Done updating credentials for {}".format(stage))
