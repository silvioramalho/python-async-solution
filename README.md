# Python Async Solution with asyncio, aiohttp and redis

This is a simple sample code created to show how I can use Asynchronous Python lib, ASYNCIO, consuming an API with AIOHTTP and writing the results in REDIS.

`Note: I am not handling exceptions yet.`

# Async Solution Sample

## Install Solution

### Clone Solution

> git clone git@github.com:silvioramalho/python-async-solution.git

> cd python-async-solution

> python3 -m venv env

> . env/bin/activate

> pip install --upgrade pip

> pip install -r requirements.txt


## Create Docker with REDIS

> docker-compose up -d

`Note: You can change the password within docker-compose.yml before running this command. Remember to change it also within the code(Line 10).`

### Current Connection Info

```
host: localhost
port: 6379
password = kjhKJHg4!
```

## Run Application 

> python src/app.py




# REDIS - CLI

## Install

> brew install redis

## Access

> redis-cli

> auth Redis2019!

* Subscribe

> SUBSCRIBE CHANNEL

* Publish

> PUBLISH CHANNEL "TEXT"



