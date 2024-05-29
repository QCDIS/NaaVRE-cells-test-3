
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_of_ints', action='store', type=str, required=True, dest='list_of_ints')


args = arg_parser.parse_args()
print(args)

id = args.id

list_of_ints = json.loads(args.list_of_ints)




for i in list_of_ints:
    a = i -1
    print(a)
a = 0.9664728952675541

file_a = open("/tmp/a_" + id + ".json", "w")
file_a.write(json.dumps(a))
file_a.close()
