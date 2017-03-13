# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys

from tweetbot import settings

class Bot(object):
	def __init__(self):
		self._client = Client(settings.keys)
	
	def run(self):
		
		return

def reply_to():
	def wrapper(func):
		# func(ID)
		return func
	return wrapper

def listen_to(matchstr):
	def wrapper(func):
		
		return
	return wrapper


