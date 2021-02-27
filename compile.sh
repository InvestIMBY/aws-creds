#!/bin/bash

if [ ! -d ".venv" ] 
then
  echo "Initializing virtual environment"
  pyenv global 3.7.9
  python -m venv .venv
else
  echo "aws-creds venv already exists"
fi

echo "Selecting aws-creds environment"
source .venv/bin/activate
pip install -r requirements.txt

echo "Generating executable"
pyinstaller --onefile --clean aws-creds.py 
sudo mv dist/aws-creds /usr/local/bin
echo "Moved aws-creds to /usr/local/bin"
