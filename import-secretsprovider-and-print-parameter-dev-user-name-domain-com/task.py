
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_number', action='store', type=int, required=True, dest='param_number')

args = arg_parser.parse_args()
print(args)

id = args.id


param_number = args.param_number


print(param_number)
a = 0.8618596350233235

