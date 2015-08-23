#!/usr/bin/python

import sys, os, re
from flask import Response, jsonify
from werkzeug.datastructures import FileStorage
from flask.ext.restful import reqparse, Resource

sys.path.append('/childlabourapi/')
from config import config

class CountryList(Resource):

	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries
	# TODO: util function - pull files from directory - end with a pattern, pattern arg
	def get(self):
		files = os.listdir(config['DATA_PATH'])			
		countries = [re.sub(r'\.json', '', f) for f in files if f.endswith('.json')]
		response = jsonify(countries = countries)
		response.status_code = 200
		return response



	