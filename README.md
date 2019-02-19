This project tests the basic functionalities of [jsonapi_requests](https://github.com/socialwifi/jsonapi-requests)

### pre-requisites:
1. Python 3
1. Virtualenv

### install requirements:
1. create and activate the python3 environment

    `virtualenv -p python3 envname`
    `source envname/bin/activate`
    
1. install project requirements

    `pip install -r requirements.txt`
   
1. run the flask server

    `export FLASK_ENV=flask_app.py`
    `flask run`
    
1. in a separate terminal session, generate the jsonapi-requests request

    `python app.py`
    
That should be enough to get you started
  


