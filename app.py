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

@app.route('/webhook', methods= ['GET', 'POST'])
def index():
    body = request.json
    name = body['queryResult']['parameters']['person']
    api_url = (f'https://api.genderize.io?name={name}')
    headers = {'Content-Type': 'text/json'}
    response = requests.get(api_url, headers= headers)
    final = response.json()

    name_given = str(final['name'])
    gender_pred = str(final['gender'])
    prob_pred = str(int(final['probability']))

    reply = '{ "fulfillmentMessages": [ { "text": { "text": [ "The gender of '+ name_given +", "+ ' is ' + gender_pred + '" ] } } ] }'

    return reply