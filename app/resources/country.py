#!/usr/bin/python
import sys, os, errno
from flask import Response, jsonify, json
from flask.ext.restful import Resource
import json

sys.path.append('/childlabourapi/')
from config import config

class Country(Resource):
	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries/<country_name>
	# e.g., curl http://localhost:5000/childlabourapi/v1/countries/afghanistan
	def get(self,country_name):
		try:
			f = open(config['DATA_PATH'] + '/' + country_name + '.json', 'r')
			return Response(f, status=200, mimetype='text/plain')	# TODO - is this the correct mimetype??
		except OSError as e:		
			if e.errno != errno.ENOENT:
				raise

	
class Description(Resource):
	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries/<country_name>/description
	def get(self,country_name):
		f = open(config['DATA_PATH'] + '/' + country_name + '.json', 'r')
		country = json.load(f)
		response = jsonify(description = country[unicode('Description')])
		response.status_code = 200
		return response

class AdvancementLevel(Resource):
	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries/<country_name>/advancement_level
	def get(self,country_name):
		f = open(config['DATA_PATH'] + '/' + country_name + '.json', 'r')
		country = json.load(f)
		response = jsonify(advancement_level = country[unicode('Advancement_Level')])
		response.status_code = 200
		return response

class CountryStatistics(Resource):
	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries/<country_name>/country_statistics
	def get(self,country_name):
		f = open(config['DATA_PATH'] + '/' + country_name + '.json', 'r')
		country = json.load(f)
		response = jsonify(country_statistics = country[unicode('Country_Statistics')])
		response.status_code = 200
		return response

class MasterData(Resource):
	# Sample usage: curl http://localhost:5000/childlabourapi/v1/countries/<country_name>/master_data
	def get(self,country_name):
		f = open(config['DATA_PATH'] + '/' + country_name + '.json', 'r')
		country = json.load(f)
		response = jsonify(master_data = country[unicode('Master_Data')])
		response.status_code = 200
		return response