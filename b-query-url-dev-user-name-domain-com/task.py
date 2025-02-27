from IPython.display import display
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--selected_hab_abb', action='store', type=str, required=True, dest='selected_hab_abb')

arg_parser.add_argument('--param_habitat_name', action='store', type=str, required=True, dest='param_habitat_name')

args = arg_parser.parse_args()
print(args)

id = args.id

selected_hab_abb = args.selected_hab_abb.replace('"','')

param_habitat_name = args.param_habitat_name.replace('"','')


url_txt = f"http://opendap.biodt.eu/ias-pdt/0/outputs/hab{selected_hab_abb}/predictions/Prediction_Summary_Shiny.txt"
df_mod = pd.read_csv(url_txt, sep="\t")
display(df_mod)
habitat_number = str(df_mod[df_mod["hab_name"] == param_habitat_name]["hab_abb"].values[0] )

file_url_txt = open("/tmp/url_txt_" + id + ".json", "w")
file_url_txt.write(json.dumps(url_txt))
file_url_txt.close()
file_habitat_number = open("/tmp/habitat_number_" + id + ".json", "w")
file_habitat_number.write(json.dumps(habitat_number))
file_habitat_number.close()
