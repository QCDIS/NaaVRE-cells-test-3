
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




names = ["Alice", "Bob"]

file_names = open("/tmp/names_" + id + ".json", "w")
file_names.write(json.dumps(names))
file_names.close()
