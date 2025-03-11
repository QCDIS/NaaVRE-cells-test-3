
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_word = os.getenv('secret_word')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')

arg_parser.add_argument('--param_greeting', action='store', type=str, required=True, dest='param_greeting')

args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)

param_greeting = args.param_greeting.replace('"','')


for name in names:
  print(f"{param_greeting}, {name}! This is the secret word: {secret_word}")

