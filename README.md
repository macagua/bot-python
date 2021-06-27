# bot-python

An Instagram Bot for publish comments random to post.

## Download

`$ git clone https://github.com/rafaelnepomuceno00/bot-python.git`


## Install

For install you need install Geckodriver and the Python libraries:

### Geckodriver

You need install the Geckodriver, with following command:

`$ wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz`

`$ sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.28.0-linux64.tar.gz -O > /usr/bin/geckodriver'`

`$ sudo chmod +x /usr/bin/geckodriver`

`$ rm geckodriver-v0.28.0-linux64.tar.gz`


### Python libraries

You need install the Python libraries, with following command:

`$ cd bot-python`

`$ pip3 install -r requeriments.txt`

### Instagram Bot settings

You need to set the Instagram Bot settings into .env file, with following command:

`$ cp .env.example .env`

`$ nano .env`


## Run Bot

For run the Python Bot, with following command:

`$ python3 ./igBot.py`

