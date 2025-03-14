from webdav3.client import Client
from minio import Minio
import os
import laspy
import shutil
import pathlib

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--laz_files', action='store', type=str, required=True, dest='laz_files')

arg_parser.add_argument('--param_bucket_name', action='store', type=str, required=True, dest='param_bucket_name')
arg_parser.add_argument('--param_max_filesize', action='store', type=str, required=True, dest='param_max_filesize')
arg_parser.add_argument('--param_minio_server', action='store', type=str, required=True, dest='param_minio_server')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required=True, dest='param_remote_path_root')
arg_parser.add_argument('--param_remote_server_type', action='store', type=str, required=True, dest='param_remote_server_type')

args = arg_parser.parse_args()
print(args)

id = args.id

laz_files = json.loads(args.laz_files)

param_bucket_name = args.param_bucket_name.replace('"','')
param_max_filesize = args.param_max_filesize.replace('"','')
param_minio_server = args.param_minio_server.replace('"','')
param_remote_path_root = args.param_remote_path_root.replace('"','')
param_remote_server_type = args.param_remote_server_type.replace('"','')

conf_laz_compression_factor = conf_laz_compression_factor = '7'
conf_wd_opts = conf_wd_opts = {'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}
conf_local_path_split = conf_local_path_split = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'split')
conf_local_tmp = conf_local_tmp = pathlib.Path('/tmp/data')

def save_chunk_to_laz_file(in_filename, 
                           out_filename, 
                           offset, 
                           n_points):
    """Read points from a LAS/LAZ file and write them to a new file."""
    points = np.array([])
    
    with laspy.open(in_filename) as in_file:
        with laspy.open(out_filename, 
                        mode="w", 
                        header=in_file.header) as out_file:
            in_file.seek(offset)
            points = in_file.read_points(n_points)
            out_file.write_points(points)
    return out_filename

def split_strategy(filename, max_filesize):
    """Set up splitting strategy for a LAS/LAZ file."""
    with laspy.open(filename) as f:
        bytes_per_point = (
            f.header.point_format.num_standard_bytes +
            f.header.point_format.num_extra_bytes
        )
        n_points = f.header.point_count
    n_points_target = int(
        max_filesize * int(conf_laz_compression_factor) / bytes_per_point
    )
    stem, ext = os.path.splitext(filename)
    return [
        (filename, f"{stem}-{n}{ext}", offset, n_points_target)
        for n, offset in enumerate(range(0, n_points, n_points_target))
    ]


client = Client(conf_wd_opts)
minio_client = Minio(param_minio_server, secure=True)

os.makedirs(conf_local_path_split, exist_ok=True)

for file in laz_files:
    print('Splitting: '+file )
    destination_path = os.path.join(conf_local_tmp,file)
    if param_remote_server_type == 'webdav':
        client.download_sync(remote_path=os.path.join(param_remote_path_root,file), local_path=destination_path)
    elif param_remote_server_type == 'minio':
        minio_client.fget_object(param_bucket_name, os.path.join(param_remote_path_root,file), destination_path)
        print(f"Downloaded: {file} to {destination_path}")
        
    inps = split_strategy(destination_path, int(param_max_filesize)*1048576)
    
    for inp in inps:
        out_filename = save_chunk_to_laz_file(*inp)
        print('out_filename: '+out_filename)
        split_path = os.path.join(conf_local_path_split,os.path.basename(out_filename))
        if os.path.exists(split_path):
            os.remove(split_path)
        shutil.move(out_filename, conf_local_path_split)

S2_done = 'True'

file_S2_done = open("/tmp/S2_done_" + id + ".json", "w")
file_S2_done.write(json.dumps(S2_done))
file_S2_done.close()
