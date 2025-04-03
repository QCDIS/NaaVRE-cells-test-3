from minio import Minio
import pathlib

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_local_root = '/tmp/data'

conf_local_knmi = '/tmp/data/knmi'

conf_local_odim = '/tmp/data/odim'

conf_local_vp = '/tmp/data/vp'

conf_local_conf = '/tmp/data/conf'

conf_local_radar_db = '/tmp/data/conf/OPERA_RADARS_DB.json'

conf_minio_endpoint = 'scruffy.lab.uvalight.net:9000'

conf_minio_public_bucket_name = 'naa-vre-public'

conf_minio_public_conf_radar_db_object_name = 'vl-vol2bird/conf/OPERA_RADARS_DB.json'


conf_local_root = '/tmp/data'
conf_local_knmi = '/tmp/data/knmi'
conf_local_odim = '/tmp/data/odim'
conf_local_vp = '/tmp/data/vp'
conf_local_conf = '/tmp/data/conf'
conf_local_radar_db = '/tmp/data/conf/OPERA_RADARS_DB.json'
conf_minio_endpoint = 'scruffy.lab.uvalight.net:9000'
conf_minio_public_bucket_name = 'naa-vre-public'
conf_minio_public_conf_radar_db_object_name = 'vl-vol2bird/conf/OPERA_RADARS_DB.json'

for local_dir in [
    conf_local_root,
    conf_local_knmi,
    conf_local_odim,
    conf_local_vp,
    conf_local_conf,
]:
    local_dir = pathlib.Path(local_dir)
    if not local_dir.exists():
        local_dir.mkdir(parents=True, exist_ok=True)
if not pathlib.Path(conf_local_radar_db).exists():

    minioClient = Minio(
        endpoint=conf_minio_endpoint,
        access_key=secret_minio_access_key,
        secret_key=secret_minio_secret_key,
        secure=True,
    )
    print(f"{conf_local_radar_db} not found, downloading")
    minioClient.fget_object(
        bucket_name=conf_minio_public_bucket_name,
        object_name=conf_minio_public_conf_radar_db_object_name,
        file_path=conf_local_radar_db,
    )

init_complete = "Yes"  # Cant sent bool
print("Finished initialization")

file_init_complete = open("/tmp/init_complete_" + id + ".json", "w")
file_init_complete.write(json.dumps(init_complete))
file_init_complete.close()
