from flask import Flask, jsonify
from flask import request


from tvgenie import getEPGData

app = Flask(__name__)




@app.route('/')
def hello():
    return jsonify({"status" : "running",
    "usage" : "GET: /schedule?channel=star-plus"})






@app.route('/schedule')
def schedule():
    channel =  request.args.get('channel')
    if channel is not None:
        return jsonify(getEPGData(channel)) 
    else:
        return jsonify({"error" : "No Channel Provided in the url"})

