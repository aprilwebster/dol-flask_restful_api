#!/usr/bin/python

import os, sys
import json
sys.path.append('/child_labour_napi/')
from config import config

def get_file_from_dir(self):
	files = (next(os.walk(config['DATA_PATH']))[2])
	pattern = ".+\.(json|txt|csv)$"	 			
	data_files = [str(f) for f in files if re.search(pattern,f)]
	response = jsonify(files = data_files)
	response.status_code = 200
	return response


def save_file(file_string, filename, path):
	file_json = json.dumps(file_string)
	if not os.path.exists(config[path]):
	    os.mkdir(config[path])
	with open(config[path] + "/" + str(filename) + '.json', 'wb') as f:
		f.write(file_json)
	f.close()
