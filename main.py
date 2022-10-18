from flask import Flask, jsonify
from flask import request


from tvgenie import getEPGData

app = Flask(__name__)




@app.route('/')
def hello():
    return 'API is up and Running Usage - GET: /schedule?channel=marvel-hq'






@app.route('/schedule')
def schedule():
    channel =  request.args.get('channel')
    return jsonify(getEPGData(channel)) 

