from laserfarm import GeotiffWriter
import os
import pathlib

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--S5_done', action='store', type=str, required=True, dest='S5_done')


args = arg_parser.parse_args()
print(args)

id = args.id

S5_done = args.S5_done.replace('"','')


conf_local_path_geotiff = conf_local_path_geotiff = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'geotiff')
conf_local_path_targets = conf_local_path_targets = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'targets')
conf_feature_name = conf_feature_name = 'perc_95_normalized_height'
conf_remote_path_geotiffs = conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' + '' + '/geotiffs')
conf_wd_opts = conf_wd_opts = {'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}

S5_done

geotiff_export_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_targets,
         'output_folder': conf_local_path_geotiff
        },
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': conf_remote_path_geotiffs.as_posix(),
}

writer = GeotiffWriter(input_dir=conf_feature_name, bands=conf_feature_name, label=conf_feature_name).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

remote_path_geotiffs = str(conf_remote_path_geotiffs)
S6_done = 'True'

file_S6_done = open("/tmp/S6_done_" + id + ".json", "w")
file_S6_done.write(json.dumps(S6_done))
file_S6_done.close()
