import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




conf_data_folder = os.path.join('/tmp','data')

conf_feature_name = 'perc_95_normalized_height'
conf_validate_precision = '0.001'
conf_tile_mesh_size = '10.'
conf_filter_type= 'select_equal'
conf_attribute = 'raw_classification'
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_apply_filter_value = '1'
conf_laz_compression_factor = '7'
conf_max_filesize = '262144000'  # desired max file size (in bytes)

