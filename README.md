# shopers_store_api_1
[![Build Status](https://travis-ci.com/araaliFarooq/shopers_store_api_1.svg?branch=master)](https://travis-ci.com/araaliFarooq/shopers_store_api_1)
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/shopers_store_api_1/badge.svg?branch=master)](https://coveralls.io/github/araaliFarooq/shopers_store_api_1?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b3c666411f5a4051a6fcf42cabeef830)](https://www.codacy.com/app/araaliFarooq/shopers_store_api_1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/shopers_store_api_1&amp;utm_campaign=Badge_Grade)

## About
This is an API of an application to manage and record transcations of a shopping store

## Heroku demo link
https://shopers-store.herokuapp.com/

## Features 
- Fetch all products
- Fetch a single product record
- Fetch all sale records
- Fetch a single sale record
- Create a product
- Create a sale order


## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
## Requirements
Python 3.6.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/shopers_store_api_1
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```
    $ cd hopers_store_api_1
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```

#### Endpoints to create, views available products and create sale records
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/products | False | Create a product
POST | /api/v1/sales | False | Create a sale order
GET | /api/v1/products | False | Fetch all available products
GET | /api/v1/products/<product_id> | False | Fetch details of a single product
GET | /api/v1/sales/<sale_id>/answer | False | Fetch details of a single sale record
GET | /api/v1/sales | False | Fetch all sale records created

## Authors
[Araali Sseruwu Farooq](https://github.com/araalifarooq)
