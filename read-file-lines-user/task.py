from os import listdir
from os.path import isfile
from os.path import join
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--file_path', action='store', type=str, required=True, dest='file_path')


args = arg_parser.parse_args()
print(args)

id = args.id

file_path = args.file_path.replace('"','')


conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')

onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)

f = open(file_path, 'r')
f.close()

