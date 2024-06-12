import os

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=int, required=True, dest='a')


args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a



print(a)
cmd = "vol2bird --version"

msg = os.system(cmd)  # returns the exit code in unix

a = 0.7065859174664395

import json
filename = "/tmp/msg_" + id + ".json"
file_msg = open(filename, "w")
file_msg.write(json.dumps(msg))
file_msg.close()
