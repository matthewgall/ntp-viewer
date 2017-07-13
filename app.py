#!/usr/bin/env python

import sys, os, logging, json, ntplib, argparse
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from time import ctime

def fetch_time():
	try:
		c = ntplib.NTPClient()
		return c.request(os.getenv('APP_SERVER', 'localhost'), version=3)
	except NTPException:
		return False

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='views/static')

@route('/favicon.ico')
def static_favicon():
	response.content_type = 'image/x-icon'
	return static_file("favicon.ico", root='views/static')

@route('/api/update')
def get_delay():
	data = {
		"timestamp": "{} UTC".format(ctime(fetch_time().tx_time)),
		"offset": "{}s".format(format(fetch_time().offset, '.15f')),
		"delay": "{}s".format(format(fetch_time().delay, '.15f'))
	}
	response.content_type = 'application/json'
	return json.dumps(data)

@route('/')
def index():
	return template("index", host=os.getenv('APP_SERVER', 'localhost'), response=fetch_time())

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	# Server settings
	parser.add_argument("-i", "--host", default=os.getenv('IP', '127.0.0.1'), help="IP Address")
	parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="Port")

	# Verbose mode
	parser.add_argument("--verbose", "-v", help="increase output verbosity", action="store_true")
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)
	log = logging.getLogger(__name__)

	try:
		app = default_app()
		app.run(host=args.host, port=args.port, server='tornado')
	except:
		log.error("Unable to start server on {}:{}".format(args.host, args.port))