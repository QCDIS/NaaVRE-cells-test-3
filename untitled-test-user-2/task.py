import numpy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

 = os.getenv('')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--', action='store', type=str, required=True, dest='')

arg_parser.add_argument('--', action='store', type=str, required=True, dest='')

args = arg_parser.parse_args()
print(args)

id = args.id

 = json.loads(args.)

print(args.)
print(type(args.))
try:
     = json.loads(args.)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
         = ast.literal_eval(args..replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e

 = 

numpy.random.random()

file_ = open("/tmp/_" + id + ".json", "w")
file_.write(json.dumps())
file_.close()
