#!/usr/bin/env python3

#from threading import Thread

from tweetbot.bot import Bot
import aesc

def main():
	bot = Bot()
	bot.setkeys(aesc.CK, aesc.CS, aesc.AT, aesc.AS)
	bot.run()

if __name__ == '__main__':
	main()

