
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_data_source_example1_name_API_key = os.getenv('secret_data_source_example1_name_API_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




print(secret_data_source_example1_name_API_key)

