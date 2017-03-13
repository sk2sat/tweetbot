from setuptools import setup, find_packages
from tweetbot import __author__, __version__, __license__

setup(
	name		= 'tweetbot',
	version		= __version__,
	description	= 'simple bot lib for twitter',
	license		= __license__,
	author		= __author__,
	author_email	= '',
	url		= 'https://github.com/sk2sat/tweetbot.git',
	keywords	= 'twitter bot',
	packages	= find_packages(),
	install_requires= [],
	)
