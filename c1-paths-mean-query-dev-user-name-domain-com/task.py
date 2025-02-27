import os
import pandas as pd
import shutil

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--habitat_number', action='store', type=str, required=True, dest='habitat_number')

arg_parser.add_argument('--url_txt', action='store', type=str, required=True, dest='url_txt')

arg_parser.add_argument('--param_climate_model', action='store', type=str, required=True, dest='param_climate_model')
arg_parser.add_argument('--param_species_class', action='store', type=str, required=True, dest='param_species_class')

args = arg_parser.parse_args()
print(args)

id = args.id

habitat_number = args.habitat_number.replace('"','')
url_txt = args.url_txt.replace('"','')

param_climate_model = args.param_climate_model.replace('"','')
param_species_class = args.param_species_class.replace('"','')




df_mod = pd.read_csv(url_txt, sep="\t")

filtered_df = df_mod[
    (df_mod["hab_abb"] == habitat_number) &
    (df_mod["climate_model"] == param_climate_model) &
    (df_mod["class"] == param_species_class) 
]



grouped_tif_paths = filtered_df.groupby("time_period")["tif_path_mean"].agg(list).to_dict()



base_dir = "output_tif_groups"
shutil.rmtree(base_dir)
os.makedirs(base_dir, exist_ok=True)

year_paths = []
for year, paths in grouped_tif_paths.items():
    year_dir = os.path.join(base_dir, str(year))  # Create a folder for each year
    os.makedirs(year_dir, exist_ok=True)  # Ensure folder exists
    year_paths.append(year_dir)
    file_path = os.path.join(year_dir, f"{year}_tif_paths.txt")  # File name
    with open(file_path, "w") as f:
        for path in paths:
            f.write(path + "\n")  # Write each path on a new line

    print(f"Saved {len(paths)} paths for {year} in {file_path}")

file_year_paths = open("/tmp/year_paths_" + id + ".json", "w")
file_year_paths.write(json.dumps(year_paths))
file_year_paths.close()
