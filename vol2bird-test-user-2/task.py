import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--{'name': 'a', 'type': 'int'}', action='store', type=int, required=True, dest='{'name': 'a', 'type': 'int'}')


args = arg_parser.parse_args()
print(args)

id = args.id

{'name': 'a', 'type': 'int'} = args.{'name': 'a', 'type': 'int'}



print(a)
cmd = "vol2bird --version"

msg = os.system(cmd)  # returns the exit code in unix

file_{'name': 'msg', 'type': 'str'} = open("/tmp/{'name': 'msg', 'type': 'str'}_" + id + ".json", "w")
file_{'name': 'msg', 'type': 'str'}.write(json.dumps({'name': 'msg', 'type': 'str'}))
file_{'name': 'msg', 'type': 'str'}.close()
