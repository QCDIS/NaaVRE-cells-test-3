import requests

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id







url = "https://github.com/mommermi/geotiff_sample/raw/master/sample.tif"
filename = "/tmp/data/sample.tif"

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)




download_done = 'True'

import json
filename = "/tmp/filename_" + id + ".json"
file_filename = open(filename, "w")
file_filename.write(json.dumps(filename))
file_filename.close()
filename = "/tmp/download_done_" + id + ".json"
file_download_done = open(filename, "w")
file_download_done.write(json.dumps(download_done))
file_download_done.close()
