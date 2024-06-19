
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--msg', action='store', type=str, required=True, dest='msg')


args = arg_parser.parse_args()
print(args)

id = args.id

msg = args.msg.replace('"','')




list_of_paths = ["/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname"]
list_of_ints = [1,2,35,6,65]
print(msg)
a = 0.3651129632175567

import json
filename = "/tmp/list_of_paths_" + id + ".json"
file_list_of_paths = open(filename, "w")
file_list_of_paths.write(json.dumps(list_of_paths))
file_list_of_paths.close()
filename = "/tmp/list_of_ints_" + id + ".json"
file_list_of_ints = open(filename, "w")
file_list_of_ints.write(json.dumps(list_of_ints))
file_list_of_ints.close()
