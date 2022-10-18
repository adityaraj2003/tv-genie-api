from flask import Flask, request, jsonify


from tvgenie import getEPGData

app = Flask(__name__)




@app.route('/')
def hello():
    return 'API is up and Running Usage - GET: /schedule?channel=marvel-hq'






@app.route('/schedule', methods = ['POST' , 'GET'])
def schedule():
    if 1 == 1:
        return jsonify(getEPGData("marvel-hq"))
    else:
        return jsonify({"error": "Usage : /schedule?channel=marvel-hq"})


