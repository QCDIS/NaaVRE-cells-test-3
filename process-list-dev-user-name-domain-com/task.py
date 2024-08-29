
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_list', action='store', type=str, required=True, dest='my_list')


args = arg_parser.parse_args()
print(args)

id = args.id

my_list = json.loads(args.my_list)




for elem in my_list:
    print(elem)

