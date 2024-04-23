import os
from sys import exit, stdout
from time import sleep
import boto3
from dotenv import load_dotenv
from paramiko import (AuthenticationException, AutoAddPolicy, SSHClient, SSHException)

load_dotenv()



with open("FE_STAGE.pem","w") as file:
    file.write(os.getenv("FE_STAGE"))  # type: ignore
fe_stage_file=(os.path.abspath("FE_STAGE.pem"))

with open("BE_STAGE.pem","w") as file:
    file.write(os.getenv("BE_STAGE"))  # type: ignore
be_stage_file=(os.path.abspath("BE_STAGE.pem"))




ec2 = boto3.client('ec2',
                   'eu-west-2',
                   aws_access_key_id=os.getenv("aws_key"),
                   aws_secret_access_key=os.getenv("aws_access_key"))

#backend
response = ec2.start_instances(InstanceIds=["i-0f89a71a4661113ba"])
sleep(5)
res = ec2.describe_instances(InstanceIds=["i-0f89a71a4661113ba"])
ip_backend=res["Reservations"][0]["Instances"][0]["PublicIpAddress"]
print(ip_backend)

#frontend
response = ec2.start_instances(InstanceIds=["i-0eadd0fdceb7eaa11"])
sleep(5)
res = ec2.describe_instances(InstanceIds=["i-0eadd0fdceb7eaa11"])
ip_frontend=res["Reservations"][0]["Instances"][0]["PublicIpAddress"]
print(ip_frontend)

sleep(20)

# backend 
try:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    #BACKEND STAGE
    client.connect(ip_backend,username='ubuntu', key_filename="BE_STAGE.pem", passphrase='mysshkeypassphrase',timeout=40)
except TimeoutError:
    print("error server backend")
    exit()
#pull repo
stdin, stdout, stderr = client.exec_command('cd ~/quirked-up-software;git restore .;git pull origin Deploy')

#apaga processo anterior
stdin, stdout, stderr = client.exec_command('cd ~/quirked-up-software/DEV/backend/main;cat save.pid')
pid=stdout.readline()[:-1]
stdin, stdout, stderr = client.exec_command(f'kill {pid}')

#instala requirements
stdin, stdout, stderr = client.exec_command(f'cd ~/quirked-up-software/DEV/backend;pip install -r requirements.txt;')

#inicia api django
stdin, stdout, stderr = client.exec_command(f'cd ~/quirked-up-software/DEV/backend/main/main;echo -e \"API_IP={ip_backend}\\nREACT_IP={ip_frontend}\" > .env')
stdin, stdout, stderr = client.exec_command(f'cd ~/quirked-up-software/DEV/backend/main;python3 manage.py reset_db --noinput;python3 manage.py makemigrations --merge --noinput;python3 manage.py migrate;python3 manage.py runscript init_db;gunicorn -p save.pid main.wsgi -b 0.0.0.0:8081 --daemon')

sleep(2)

#verifica se o processo existe (forma para ver se o processo correu)
stdin, stdout, stderr = client.exec_command('cd ~/quirked-up-software/DEV/backend/main;cat save.pid')
pid=stdout.readline()[:-1]
stdin, stdout, stderr = client.exec_command(f'ps -p {pid}')
if len(stdout.readlines())>1:
    print("success")
else:
    print("error")

client.close()

try:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    #FRONTEND STAGE
    client.connect(ip_frontend,username='ubuntu', key_filename="FE_STAGE.pem", passphrase='mysshkeypassphrase',timeout=40)
except TimeoutError:
    print("error server frontend")
    client.close()
    exit()

#pull repo
stdin, stdout, stderr = client.exec_command('cd ~/quirked-up-software;git restore .;git pull origin Deploy')

#apaga processo anterior
client.exec_command('cd ~/quirked-up-software/DEV/frontend/;pm2 delete all')

#inicia react
stdin, stdout, stderr = client.exec_command(f'cd ~/quirked-up-software/DEV/frontend;npm install;npm run build')
result=stdout.read().decode("utf-8")
if (result.find("Failed")==-1):
    stdin, stdout, stderr = client.exec_command(f'cd ~/quirked-up-software/DEV/frontend;echo \"REACT_APP_API={ip_backend}\" > .env;pm2 --name Project start npm -- run start_deploy')
    print(f"success\nhttp://{ip_frontend}:8080")
else:
    print("error")
    print(result)

client.close()

os.remove(fe_stage_file)
os.remove(be_stage_file)