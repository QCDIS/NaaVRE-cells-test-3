from matplotlib import pyplot
import rasterio
import requests
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
import papermill as pm

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id
parameters = {}




pm.execute_notebook(
    'task.ipynb',
    'task-output.ipynb',
    prepare_only=True,
    parameters=dict(parameters)
)

import json
filename = "/tmp/filename_" + id + ".json"
file_filename = open(filename, "w")
file_filename.write(json.dumps(filename))
file_filename.close()
