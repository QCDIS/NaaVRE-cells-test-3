
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
param_list_str = ["list_str", "space in elem", "3"]

conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'  # comment
conf_int = 1
conf_float = 1.1
conf_list_int = [1, 2, 3]
conf_list_str = ["list_str", "space in elem", "3"]

var_string = 'var_string value'
var_string_with_comment = 'var_string value'  # comment
var_int = 1
var_float = 1.1
var_list_int = [1, 2, 3]
var_list_str = ["list_str", "space in elem", "3"]
a = 0.3199420717307375

file_var_string = open("/tmp/var_string_" + id + ".json", "w")
file_var_string.write(json.dumps(var_string))
file_var_string.close()
file_var_string_with_comment = open("/tmp/var_string_with_comment_" + id + ".json", "w")
file_var_string_with_comment.write(json.dumps(var_string_with_comment))
file_var_string_with_comment.close()
file_var_int = open("/tmp/var_int_" + id + ".json", "w")
file_var_int.write(json.dumps(var_int))
file_var_int.close()
file_var_float = open("/tmp/var_float_" + id + ".json", "w")
file_var_float.write(json.dumps(var_float))
file_var_float.close()
file_var_list_int = open("/tmp/var_list_int_" + id + ".json", "w")
file_var_list_int.write(json.dumps(var_list_int))
file_var_list_int.close()
file_var_list_str = open("/tmp/var_list_str_" + id + ".json", "w")
file_var_list_str.write(json.dumps(var_list_str))
file_var_list_str.close()
