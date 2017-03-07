from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys


class Bot:
	def __init__(self):
		self.CK = ''
		self.CS = ''
		self.AT = ''
		self.AS = ''
	
	def run(self):
		url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		session = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
		res = session.get(url, params = {'user_id':'1162683152', 'count':10})
		if res.status_code != 200:
			print('error')
			sys.exit(1)
		print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
		print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
		sec = int(res.headers['X-Rate-Limit-Reset'])\
		           - time.mktime(datetime.datetime.now().timetuple())
		print ('リセット時間 （残り秒数に換算） %s' % sec)
		
		#--------------
		# テキスト部
		#--------------
		res_text = json.loads(res.text)
		for tweet in res_text:
			print ('-----')
			print (tweet['created_at'])
			print (tweet['text'])
		sys.exit(0)
		return
	
	def setkeys(self, CK, CS, AT, AS):
		self.CK = CK
		self.CS = CS
		self.AT = AT
		self.AS = AS


