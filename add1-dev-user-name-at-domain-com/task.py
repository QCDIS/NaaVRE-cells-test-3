
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--count', action='store', type=int, required=True, dest='count')


args = arg_parser.parse_args()
print(args)

id = args.id

count = args.count




a = count + 1
a = 0.25829842685683957

import json
filename = "/tmp/a_" + id + ".json"
file_a = open(filename, "w")
file_a.write(json.dumps(a))
file_a.close()
