
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_v = open("/tmp/v_" + id + ".json", "w")
file_v.write(json.dumps(v))
file_v.close()
