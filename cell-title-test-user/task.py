import math as m
from math import nan

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_test = os.getenv('secret_test')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=int, required=True, dest='a')

arg_parser.add_argument('--b', action='store', type=float, required=True, dest='b')

arg_parser.add_argument('--c', action='store', type=str, required=True, dest='c')

arg_parser.add_argument('--d', action='store', type=str, required=True, dest='d')

arg_parser.add_argument('--e', action='store', type=float, required=True, dest='e')

arg_parser.add_argument('--param_test', action='store', type=str, required=True, dest='param_test')

args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a
b = args.b
c = args.c.replace('"','')
d = json.loads(args.d)
e = args.e

param_test = args.param_test.replace('"','')


print(param_test, secret_test, a, b, c, d, e)
f = [m.pi, nan]

file_f = open("/tmp/f_" + id + ".json", "w")
file_f.write(json.dumps(f))
file_f.close()
