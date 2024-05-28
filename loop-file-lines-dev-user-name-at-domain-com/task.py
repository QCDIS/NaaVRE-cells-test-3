
import argparse
import json
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--lines', action='store', type=str, required=True, dest='lines')


args = arg_parser.parse_args()
print(args)

id = args.id

lines = json.loads(args.lines)




count = 0
for l in lines:
    count += 1
    print("Line{}: {}".format(count, l.strip()))
a = 0.06129452201313035

file_count = open("/tmp/count_" + id + ".json", "w")
file_count.write(json.dumps(count))
file_count.close()
