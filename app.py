#!/usr/bin/env python

import sys, os, logging, json, ntplib
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from time import ctime

def fetch_time():
	c = ntplib.NTPClient()
	return c.request(os.getenv('APP_SERVER', 'localhost'), version=3)

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='views/static')

@route('/api/time')
def get_time():
	return "{} UTC".format(ctime(fetch_time().tx_time))

@route('/')
def index():
	return template("index", response=fetch_time())

if __name__ == '__main__':
	app = default_app()

	serverHost = os.getenv('IP', 'localhost')
	serverPort = os.getenv('PORT', '5000')

	# Now we're ready, so start the server
	# Instantiate the logger
	log = logging.getLogger('log')
	console = logging.StreamHandler()
	log.setLevel(logging.INFO)
	log.addHandler(console)

	# Now we're ready, so start the server
	try:
		app.run(host=serverHost, port=serverPort, server='tornado')
	except:
		log.error("Failed to start application server")