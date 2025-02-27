import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




url = "http://opendap.biodt.eu/ias-pdt/0/outputs/key.csv"
df_hab = pd.read_csv(url)

selected_hab_abb = '1'
conf_data_path = '/tmp/data/'



folder_path = None
tif_url = None
download_path = None


param_habitat_name =  'Ruderal habitats'
habitat_type = param_habitat_name.replace(' ','_').lower()
selected_hab_abb = str(df_hab[df_hab["hab_name"] == habitat_type]["hab_abb"].values[0])
param_climate_model = 'IPSL-CM6A-LR'
param_species_class = 'Liliopsida'


conf_x =  0.95
conf_y =  0.95
conf_arrow_length = 0.1
print(f"Selected Habitat Abbreviation: {selected_hab_abb}")

file_selected_hab_abb = open("/tmp/selected_hab_abb_" + id + ".json", "w")
file_selected_hab_abb.write(json.dumps(selected_hab_abb))
file_selected_hab_abb.close()
