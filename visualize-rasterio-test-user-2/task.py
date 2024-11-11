{'asname': None, 'module': '', 'name': 'os'}
{'asname': None, 'module': '', 'name': 'pathlib'}
{'asname': None, 'module': 'matplotlib', 'name': 'pyplot'}
{'asname': None, 'module': '', 'name': 'rasterio'}
{'asname': None, 'module': 'rasterio.plot', 'name': 'show'}
{'asname': None, 'module': 'rasterio.plot', 'name': 'show_hist'}

import argparse
import papermill as pm

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--{'name': 'S6_done', 'type': 'str'}', action='store', type=str, required=True, dest='{'name': 'S6_done', 'type': 'str'}')


args = arg_parser.parse_args()
print(args)

id = args.id
parameters = {}

{'name': 'S6_done', 'type': 'str'} = args.{'name': 'S6_done', 'type': 'str'}.replace('"','')
parameters['{'name': 'S6_done', 'type': 'str'}'] = {'name': 'S6_done', 'type': 'str'}


name = conf_local_path_geotiff
parameters['name'] = name
assignation = conf_local_path_geotiff = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'geotiff')
parameters['assignation'] = assignation

pm.execute_notebook(
    'task.ipynb',
    'task-output.ipynb',
    prepare_only=True,
    parameters=dict(parameters)
)

