#!/bin/bash

if [ ! -d "/home/ec2-user/dev/venv/aws-creds" ] 
then
  echo "Initializing virtual environment"
  pyenv global 3.7.9
  python -m venv /home/ec2-user/dev/venv/aws-creds
else
  echo "aws-creds venv already exists"
fi

echo "Selecting aws-creds"
source /home/ec2-user/dev/venv/aws-creds/bin/activate
pip install -r requirements.txt