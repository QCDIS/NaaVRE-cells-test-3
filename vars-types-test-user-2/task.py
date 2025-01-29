
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

file_{'name': 'var_string', 'type': 'str'} = open("/tmp/{'name': 'var_string', 'type': 'str'}_" + id + ".json", "w")
file_{'name': 'var_string', 'type': 'str'}.write(json.dumps({'name': 'var_string', 'type': 'str'}))
file_{'name': 'var_string', 'type': 'str'}.close()
file_{'name': 'var_string_with_comment', 'type': 'str'} = open("/tmp/{'name': 'var_string_with_comment', 'type': 'str'}_" + id + ".json", "w")
file_{'name': 'var_string_with_comment', 'type': 'str'}.write(json.dumps({'name': 'var_string_with_comment', 'type': 'str'}))
file_{'name': 'var_string_with_comment', 'type': 'str'}.close()
file_{'name': 'var_int', 'type': 'int'} = open("/tmp/{'name': 'var_int', 'type': 'int'}_" + id + ".json", "w")
file_{'name': 'var_int', 'type': 'int'}.write(json.dumps({'name': 'var_int', 'type': 'int'}))
file_{'name': 'var_int', 'type': 'int'}.close()
file_{'name': 'var_float', 'type': 'float'} = open("/tmp/{'name': 'var_float', 'type': 'float'}_" + id + ".json", "w")
file_{'name': 'var_float', 'type': 'float'}.write(json.dumps({'name': 'var_float', 'type': 'float'}))
file_{'name': 'var_float', 'type': 'float'}.close()
file_{'name': 'var_list_int', 'type': 'list'} = open("/tmp/{'name': 'var_list_int', 'type': 'list'}_" + id + ".json", "w")
file_{'name': 'var_list_int', 'type': 'list'}.write(json.dumps({'name': 'var_list_int', 'type': 'list'}))
file_{'name': 'var_list_int', 'type': 'list'}.close()
file_{'name': 'var_list_str', 'type': 'list'} = open("/tmp/{'name': 'var_list_str', 'type': 'list'}_" + id + ".json", "w")
file_{'name': 'var_list_str', 'type': 'list'}.write(json.dumps({'name': 'var_list_str', 'type': 'list'}))
file_{'name': 'var_list_str', 'type': 'list'}.close()
