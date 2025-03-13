
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



f = open(file_path, 'r')
lines = f.readlines()
f.close()

file_lines = open("/tmp/lines_" + id + ".json", "w")
file_lines.write(json.dumps(lines))
file_lines.close()
