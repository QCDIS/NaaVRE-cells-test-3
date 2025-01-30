import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=int, required=True, dest='a')


args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a



print(a)
cmd = "KNMI_vol_h5_to_ODIM_h5 "

out = os.system(cmd)  # returns the exit code in unix

file_out = open("/tmp/out_" + id + ".json", "w")
file_out.write(json.dumps(out))
file_out.close()
