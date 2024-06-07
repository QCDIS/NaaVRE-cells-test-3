from matplotlib import pyplot
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
import papermill as pm

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--filename', action='store', type=str, required=True, dest='filename')


args = arg_parser.parse_args()
print(args)

id = args.id
parameters = {}

filename = args.filename.replace('"','')
parameters['filename'] = filename



pm.execute_notebook(
    'task.ipynb',
    'task-output.ipynb',
    prepare_only=True,
    parameters=dict(parameters)
)

