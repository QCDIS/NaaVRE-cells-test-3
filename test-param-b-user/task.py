
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_b', action='store', type=str, required=True, dest='param_b')

args = arg_parser.parse_args()
print(args)

id = args.id


param_b = args.param_b.replace('"','')


print(param_b)
b = param_b

file_b = open("/tmp/b_" + id + ".json", "w")
file_b.write(json.dumps(b))
file_b.close()
