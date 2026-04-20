
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_a', action='store', type=str, required=True, dest='param_a')

args = arg_parser.parse_args()
print(args)

id = args.id


param_a = args.param_a.replace('"','')


print(param_a)
a = param_a

file_a = open("/tmp/a_" + id + ".json", "w")
file_a.write(json.dumps(a))
file_a.close()
