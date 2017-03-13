#!/usr/bin/env python3

#from threading import Thread

from tweetbot.bot import Bot
import aesc
import sksat

def main():
	bot = Bot()
	bot.setkeys(sksat.CK, sksat.CS, sksat.AT, sksat.AS)
	bot.run()

if __name__ == '__main__':
	main()

