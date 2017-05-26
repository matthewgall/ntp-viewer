#!/usr/bin/env python

import sys, os, logging, json, ntplib
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from time import ctime

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='views/static')

@route('/')
def index():
	c = ntplib.NTPClient()
	response = c.request(os.getenv('APP_SERVER', 'localhost'), version=3)
	return template("index", response=response)

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