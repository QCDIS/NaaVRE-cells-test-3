
import argparse
import json
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




my_list = [1, 2, 3]
print(my_list)

filename = "/tmp/my_list_" + id + ".json"
file_my_list = open(filename, "w")
file_my_list.write(json.dumps(my_list))
file_my_list.close()
