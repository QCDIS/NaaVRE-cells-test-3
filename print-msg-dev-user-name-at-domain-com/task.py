
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--msg', action='store', type=int, required=True, dest='msg')


args = arg_parser.parse_args()
print(args)

id = args.id

msg = args.msg



print('msg:', str(msg))
a = 0.9840142867020398

