
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




param_string = 'param_string value'
param_string_with_comment = 'param_string value'  # comment
param_int = 1
param_float = 1.1
param_list_int = [1, 2, 3]
param_list_str = ["1", "space in elem", "3"]

conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'  # comment
conf_int = 1
conf_float = 1.1
conf_list_int = [1, 2, 3]
conf_list_str = ["conf_list_str", "space in elem", "3"]

var_string = 'var_string value'
var_string_with_comment = 'var_string value'  # comment
var_int = 1
var_float = 1.1
var_list_int = [1, 2, 3]
var_list_str = ["var_list_str", "space in elem", "3"]

