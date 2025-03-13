
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_int', action='store', type=int, required=True, dest='param_int')

args = arg_parser.parse_args()
print(args)

id = args.id


param_int = args.param_int


print(param_int)

