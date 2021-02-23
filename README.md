Note: not compatible with Python 3.8

Also, when installing 3.7.9, it needs shard libraries:
ON Linux
CONFIGURE_OPTS=--enable-shared pyenv install 3.8.7

ON MAC ...
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.7.9

# Credentials helper:

1. Create a new file in

```
~/.terraformrc

plugin_cache_dir   = "$HOME/.terraform.d/plugin-cache"
disable_checkpoint = true

credentials_helper "keychain" {
  args = []
}
```

run:

```
mkdir ~/.terraform.d/plugin-cache
mkdir ~/.terraform.d/plugins
```

2. put the `terraform-credentials-keychain` binary in the `~/.terraform.d/plugins` folder.

Have a `~/.terraform.d/credentials.tfrc.json` file with the following content to allow terraform provider to work (for now, a workaround):

```
{
  "credentials": {
    "none": {
      "token": "NxtIaFyc8FNYGA.atlasv1.fjIS0N6oIfq8mfnyxT9CMBIoUTYrhL0ztbVGlYy1E2SQUlw6ogdBqAbzbSDlVo01fZI"
    }
  }
}
```

3. Create a new keychain on your mac:

account: tf_user
where: terraform

Add your terraform token to it.

To convert a .py file into a binary run:


pipenv shell
pyinstaller --onefile --clean yourprogram.py
mv dist/yourprogram /usr/local/bin/

If having issues, try:

pyinstaller --onefile --clean --hidden-import <missing module> terraform+.py

If still having issues:

pipenv --venv

Edit the spec file generated, and add the <venv locaion>/lib/python3.7/site-packages to the 

pathex=['<orig>','<venv location']

And call:

pyinstaller --onedir --name=terraform_cred terraform_creds.spec

terraform-credentials-keychain_v1.0.0

pathex=['/Users/alonsabi/dev/serverless_tools','/Users/alonsabi/.local/share/virtualenvs/serverless_tools-vNBysnLi/lib/python3.7/site-packages'],

pyinstaller --onefile --clean terraform-credentials-keychain.py
mv dist/terraform-credentials-keychain ~/.terraform.d/plugins
