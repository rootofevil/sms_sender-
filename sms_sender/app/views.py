# -*- coding: utf-8 -*-
from app import app
from flask import redirect, url_for, request, abort, jsonify
from subprocess import call, Popen, PIPE
from tempfile import mkstemp, NamedTemporaryFile
import logging, os, shutil

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = 'smssender1.log')

@app.route('/', methods = ('GET', 'POST'))
def home():
    return "Please go to API"

@app.route('/api/v1/sendsms', methods = ['POST'])
def sendsms():
    
    if not request.json or not 'caller_id' in request.json:
        abort(400)
  
    phone = request.json['caller_id'].encode('utf-8')
    text = request.json['text'].encode('utf-16')
    alphabet = 'UCS2'
    outdir = '/var/spool/sms/outgoing/'
    
    
    file = NamedTemporaryFile(prefix='sms_', delete=False)
    msg = "To: %s\nAlphabet: %s\nUDH: false\n" % (phone, alphabet)
    if 'flash' in request.json and request.json['flash'] == 'True':
        msg += "Flash: yes\n"
        
    msg += "\n"
    file.write(msg)
    file.write(text)
    os.chmod(file.name, 0777)
    file.close()
    shutil.move(file.name, outdir)
    #logging.debug(file.name)
    #logging.debug(msg)
    
    
    result = 0
    if result == 0:
        return jsonify({'status': 'ok'}), 201
    else:
        return jsonify({'status': 'err', 'error_msg': err}), 200