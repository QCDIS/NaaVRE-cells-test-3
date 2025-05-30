
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




io_number = 1

file_io_number = open("/tmp/io_number_" + id + ".json", "w")
file_io_number.write(json.dumps(io_number))
file_io_number.close()
