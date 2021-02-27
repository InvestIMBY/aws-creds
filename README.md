# AWS Credential script

The purpose of this script is to populate temporary credentials.
If there is a .terraform folder, it also attempts to populate terraform
variables to allow terraform cloud to connect to AWS with the temporary
credentials.

When .terraform folder exists, the profile is picked based on the .terraform folder.
Usage:

aws-creds <aws profile>

The aws profile is overridden to whatever .terraform has if it exists.

Note: not compatible with Python 3.8


# Install python 3.7.9 (did not work with 3.8)

ON Linux

`CONFIGURE_OPTS=--enable-shared pyenv install 3.7.9`

ON MAC

`env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.7.9`

# Trigger initialization script and compile

It creates the virtual environment if it does not exist,
installes the required modules, triggers the compile, and
copy the executable to the /usr/local/bin folder.

`./compile.sh`

