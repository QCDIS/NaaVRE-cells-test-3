
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--sentences', action='store', type=str, required=True, dest='sentences')


args = arg_parser.parse_args()
print(args)

id = args.id

sentences = json.loads(args.sentences)



print(sentences)

