# password_generator

Python password generator

USAGE:

```
 python3 pwgen.py [--charonly] password_length
```

I have created this script so I am able to generate passwords through my shell, with its output already copied to clipboard.

In order to use this functionality you have to create an alias for your shell(configure the code for your own shell):

```
echo "alias pwgen='/path/to/python3 /path/to/pwgen.py'" >> ~/.zshrc
source ~/.zshrc
```

NOTICE:

Before using this password generator, use :

```
/path/to/pip3 install -r requirements.txt
```

IT IS ALSO IMPORTANT FOR YOUR PYTHON AND PIP PACKAGES TO BE READ FROM THE SAME PLACE IN ORDER FOR THIS TO WORK PROPERLY

-   Mac users will probably encounter this error to resolve use full path to your python and pip packages(same applies when creating alias)

    for example:

```
  /opt/homebrew/bin/pip3 install -r requirements
  /opt/homebrew/bin/python3.10 pwgen.py
```
