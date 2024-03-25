
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--lines', action='store', type=str, required=True, dest='lines')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
lines = json.loads(args.lines)




count = 0
for l in lines:
    count += 1
    print("Line{}: {}".format(count, l.strip()))

import json
filename = "/tmp/count_" + id + ".json"
file_count = open(filename, "w")
file_count.write(json.dumps(count))
file_count.close()
