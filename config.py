#!/usr/bin/python

INSTALLATION_PATH = '/Users/apester/workspace'
APP_PATH = INSTALLATION_PATH + '/child_labour_api/app'
HOST = '127.0.0.1'
PORT = '5000'
PATH = '/childlabourapi/v1'

config={
'HOST': HOST,
'PORT': PORT,
'PATH': PATH,
'API_URL': 'http://'+HOST+':'+PORT+PATH,
'DATA_DIR': '/data',
'DATA_PATH': APP_PATH+'/data'
}





