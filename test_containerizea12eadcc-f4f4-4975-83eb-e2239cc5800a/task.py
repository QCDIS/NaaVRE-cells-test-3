import pandas

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_dataverse_api_key', action='store', type=str, required=True, dest='param_dataverse_api_key')

args = arg_parser.parse_args()
print(args)

id = args.id


param_dataverse_api_key = args.param_dataverse_api_key.replace('"','')


print("doesn't work")

file_event_file = open("/tmp/event_file_" + id + ".json", "w")
file_event_file.write(json.dumps(event_file))
file_event_file.close()
