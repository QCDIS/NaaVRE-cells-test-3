from laserfarm import Retiler
import os
import pathlib

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--split_laz_files', action='store', type=str, required=True, dest='split_laz_files')


args = arg_parser.parse_args()
print(args)

id = args.id

split_laz_files = json.loads(args.split_laz_files)


conf_local_path_retiled = conf_local_path_retiled = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'retiled')
conf_local_path_split = conf_local_path_split = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'split')
conf_max_x = conf_max_x = '398892.19'
conf_max_y = conf_max_y = '726783.87'
conf_min_x = conf_min_x = '-113107.81'
conf_min_y = conf_min_y = '214783.87'
conf_n_tiles_side = conf_n_tiles_side = '512'

split_laz_files

grid_retile = {
    'min_x': float(conf_min_x),
    'max_x': float(conf_max_x),
    'min_y': float(conf_min_y),
    'max_y': float(conf_max_y),
    'n_tiles_side': int(conf_n_tiles_side)
}

retiling_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_split,
        'output_folder': conf_local_path_retiled
    },
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
}

for file in split_laz_files:
    clean_file = file.replace('"','').replace('[','').replace(']','')
    print(clean_file)
    retiler = Retiler(clean_file,label=clean_file).config(retiling_input)
    retiler_output = retiler.run()

S3_done = 'True'

file_S3_done = open("/tmp/S3_done_" + id + ".json", "w")
file_S3_done.write(json.dumps(S3_done))
file_S3_done.close()
