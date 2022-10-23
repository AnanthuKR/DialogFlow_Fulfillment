from crypt import methods
from urllib import request
from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return '{"Hello": "AIDI!"}'

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.json
    name1 = body['queryResult']['parameters']['name']
    return name1
    
    # api_url = 'https://api.genderize.io?name='+ name1
    # headers = {'Content-Type': 'application/json'}
    # response = requests.get(api_url, headers= headers)
    # final = response.json()

    # name_given = str(final['name'])
    # gender_pred = str(final['gender'])
    # prob_pred = str(int(final['probability']))

    # reply = '{ "fulfillmentMessages": [ { "text": { "text": [ "The gender of '+ name_given +", "+ ' is ' + gender_pred + '" ] } } ] }'

    # return reply