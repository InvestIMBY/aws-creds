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

