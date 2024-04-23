import os
from sys import exit, stdout
from time import sleep
import boto3
from dotenv import load_dotenv

load_dotenv()

ec2 = boto3.client('ec2',
                   'eu-west-2',
                   aws_access_key_id=os.getenv("aws_key"),
                   aws_secret_access_key=os.getenv("aws_access_key"))

#backend
response = ec2.stop_instances(InstanceIds=["i-0f89a71a4661113ba"])
#frontend
response = ec2.stop_instances(InstanceIds=["i-0eadd0fdceb7eaa11"])