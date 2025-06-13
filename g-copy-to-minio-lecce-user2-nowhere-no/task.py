from minio import Minio

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_animated_path', action='store', type=str, required=True, dest='output_animated_path')

arg_parser.add_argument('--output_gif', action='store', type=str, required=True, dest='output_gif')

arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id

output_animated_path = args.output_animated_path.replace('"','')
output_gif = args.output_gif.replace('"','')

param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')


mc = Minio(endpoint=param_minio_endpoint,
access_key=secret_minio_access_key,
secret_key=secret_minio_secret_key)

mc.fput_object(bucket_name="naa-vre-user-data", file_path=output_animated_path, object_name=param_minio_user_prefix+"/"+output_gif)

