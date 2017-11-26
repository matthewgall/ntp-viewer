#!/usr/bin/env python

import sys, os, logging, json, ntplib, argparse, time
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from time import ctime

def set_content_type(fn):
	def _return_json(*args, **kwargs):
		response.headers['Content-Type'] = 'application/json'
		if request.method != 'OPTIONS':
			return fn(*args, **kwargs)
	return _return_json

def enable_cors(fn):
	def _enable_cors(*args, **kwargs):
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
		response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

		if request.method != 'OPTIONS':
			return fn(*args, **kwargs)
	return _enable_cors

def embed_date(fn):
	def _embed_date(*args, **kwargs):
		response.set_header('Date', "{} UTC".format(time.ctime(fetch_time().tx_time)))
		if request.method != 'OPTIONS':
			return fn(*args, **kwargs)
	return _embed_date

def fetch_time():
	try:
		c = ntplib.NTPClient()
		return c.request(args.server, version=3)
	except NTPException:
		return False

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='views/static')

@route('/favicon.ico')
def static_favicon():
	response.content_type = 'image/x-icon'
	return static_file("favicon.ico", root='views/static')

@route("/.well-known/time", ('HEAD', 'GET'))
@embed_date
def get_ntphttp():
	return response.get_header('Date')

@route('/api')
@enable_cors
def get_delay():
	data = {
		"timestamp": "{} UTC".format(time.ctime(fetch_time().tx_time)),
		"offset": "{}s".format(format(fetch_time().offset, '.15f')),
		"delay": "{}s".format(format(fetch_time().delay, '.15f'))
	}
	response.content_type = 'application/json'
	return json.dumps(data)

@route('/')
@enable_cors
def index():
	return template("index", host=args.server, response=fetch_time())

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	# Server settings
	parser.add_argument("-i", "--host", default=os.getenv('IP', '127.0.0.1'), help="IP Address")
	parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="Port")

	# Time server
	parser.add_argument("-s", "--server", default=os.getenv('APP_SERVER', 'localhost'), help="address of NTP server")

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