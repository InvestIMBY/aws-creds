#!/bin/bash

source ~/dev/venv/aws-creds/bin/activate
pyinstaller --onefile --clean aws-creds.py 
sudo mv dist/aws-creds /usr/local/bin
