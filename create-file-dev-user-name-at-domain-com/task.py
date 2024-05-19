from os.path import isfile
from os.path import join
from os import listdir
import os

import argparse
import json
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_data_folder = os.path.join('/tmp','data')


conf_data_folder = os.path.join('/tmp','data')

L = ["a\n", "b\n", "c\n"]
file_path =  os.path.join(conf_data_folder,'hello.txt')
fp = open(file_path, 'w')
fp.writelines(L)
fp.close()

onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)
a = 0.26307737645757046

filename = "/tmp/file_path_" + id + ".json"
file_file_path = open(filename, "w")
file_file_path.write(json.dumps(file_path))
file_file_path.close()
