# -*- coding: utf-8 -*-
from flask import Flask
#import logging
#from logging.handlers import RotatingFileHandler

app = Flask(__name__)
#app.config.from_object('config')


#handler = RotatingFileHandler('smssender.log', maxBytes=10000, backupCount=1)
#handler.setLevel(logging.DEBUG)
#app.logger.addHandler(handler)

from app import views
