#!/usr/bin/env python3

#from threading import Thread

import twitter.bot as twitter
import aesc

def main():
	bot = twitter.Bot()
	bot.setkeys(aesc.CK, aesc.CS, aesc.AT, aesc.AS)
	bot.run()

if __name__ == '__main__':
	main()

