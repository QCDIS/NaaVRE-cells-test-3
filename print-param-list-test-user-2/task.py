
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_list', action='store', type=str, required=True, dest='param_list')

args = arg_parser.parse_args()
print(args)

id = args.id


print(args.param_list)
print(type(args.param_list))
try:
    param_list = json.loads(args.param_list)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list = ast.literal_eval(args.param_list.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e


print(param_list)

