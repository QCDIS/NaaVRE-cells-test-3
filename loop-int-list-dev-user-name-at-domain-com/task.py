
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_of_ints', action='store', type=str, required=True, dest='list_of_ints')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
list_of_ints = json.loads(args.list_of_ints)




for i in list_of_ints:
    a = i -1
    print(a)
a = 0.7780510000545949

import json
filename = "/tmp/a_" + id + ".json"
file_a = open(filename, "w")
file_a.write(json.dumps(a))
file_a.close()
