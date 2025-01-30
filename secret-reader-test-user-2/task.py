
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_xyz = os.getenv('secret_xyz')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--foo', action='store', type=str, required=True, dest='foo')

arg_parser.add_argument('--param_abc', action='store', type=str, required=True, dest='param_abc')

args = arg_parser.parse_args()
print(args)

id = args.id

foo = args.foo.replace('"','')

param_abc = args.param_abc.replace('"','')


print(param_abc, secret_xyz, foo)

