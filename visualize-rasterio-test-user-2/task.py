import os
import pathlib
from matplotlib import pyplot
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
import papermill as pm

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--S6_done', action='store', type=str, required=True, dest='S6_done')


args = arg_parser.parse_args()
print(args)

id = args.id
parameters = {}

S6_done = args.S6_done.replace('"','')
parameters['S6_done'] = S6_done


conf_local_path_geotiff = conf_local_path_geotiff = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'geotiff')
parameters['conf_local_path_geotiff'] = conf_local_path_geotiff

pm.execute_notebook(
    'task.ipynb',
    'task-output.ipynb',
    prepare_only=True,
    parameters=dict(parameters)
)

