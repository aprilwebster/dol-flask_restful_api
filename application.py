#!/usr/bin/python

from flask import Flask
from flask.ext.restful import Api

# Import config for application
from config import config

# Import all of the resources
from app.resources.countrylist import CountryList
from app.resources.country import Country
from app.resources.country import AdvancementLevel
from app.resources.country import Description
from app.resources.country import CountryStatistics
from app.resources.country import MasterData

# Create the Flask app and api
app = Flask(__name__)
api = Api(app)

# Routing information
api.add_resource(Country, config['PATH'] + '/countries/<string:country_name>')
api.add_resource(CountryList, config['PATH'] + '/countries')
api.add_resource(AdvancementLevel, config['PATH'] + '/countries/<string:country_name>/advancement_level')
api.add_resource(Description, config['PATH'] + '/countries/<string:country_name>/description')
api.add_resource(CountryStatistics, config['PATH'] + '/countries/<string:country_name>/country_statistics')
api.add_resource(MasterData, config['PATH'] + '/countries/<string:country_name>/master_data')



if __name__ == '__main__':
    #app.run(debug=False, host='0.0.0.0')		
    app.run(debug=True)						# This results in the server reloading after a change to this script