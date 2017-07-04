from app import app
from flask import redirect, url_for, request, abort, jsonify
from subprocess import call

@app.route('/', methods = ('GET', 'POST'))
def home():
    return "Please go to API"

@app.route('/api/v1/sendsms', methods = ['POST'])
def sendsms():
    if not request.json or not 'caller_id' in request.json:
        abort(400)
    msg = dict(caller_id = request.json['caller_id'], text = request.json['text'])
    #result = call(['sudo', '-u', 'smstools', 'smssend', msg['caller_id'], msg['text']])
    result = 1
    if result == 0:
        return jsonify({'status': 'ok'}), 201
    else: 
        return jsonify({'status': 'err'}), 200