
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var_float', action='store', type=float, required=True, dest='var_float')

arg_parser.add_argument('--var_int', action='store', type=int, required=True, dest='var_int')

arg_parser.add_argument('--var_list_int', action='store', type=str, required=True, dest='var_list_int')

arg_parser.add_argument('--var_list_str', action='store', type=str, required=True, dest='var_list_str')

arg_parser.add_argument('--var_string', action='store', type=str, required=True, dest='var_string')

arg_parser.add_argument('--var_string_with_comment', action='store', type=str, required=True, dest='var_string_with_comment')

arg_parser.add_argument('--param_float', action='store', type=float, required=True, dest='param_float')
arg_parser.add_argument('--param_int', action='store', type=int, required=True, dest='param_int')
arg_parser.add_argument('--param_list_int', action='store', type=str, required=True, dest='param_list_int')
arg_parser.add_argument('--param_list_str', action='store', type=str, required=True, dest='param_list_str')
arg_parser.add_argument('--param_string', action='store', type=str, required=True, dest='param_string')
arg_parser.add_argument('--param_string_with_comment', action='store', type=str, required=True, dest='param_string_with_comment')

args = arg_parser.parse_args()
print(args)

id = args.id

var_float = args.var_float
var_int = args.var_int
var_list_int = json.loads(args.var_list_int)
var_list_str = json.loads(args.var_list_str)
var_string = args.var_string.replace('"','')
var_string_with_comment = args.var_string_with_comment.replace('"','')

param_float = args.param_float
param_int = args.param_int
print(args.param_list_int)
print(type(args.param_list_int))
try:
    param_list_int = json.loads(args.param_list_int)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list_int = ast.literal_eval(args.param_list_int.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e
print(args.param_list_str)
print(type(args.param_list_str))
try:
    param_list_str = json.loads(args.param_list_str)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list_str = ast.literal_eval(args.param_list_str.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e
param_string = args.param_string.replace('"','')
param_string_with_comment = args.param_string_with_comment.replace('"','')

conf_float = 1.1

conf_int = 1

conf_list_int = [1, 2, 3]

conf_list_str = ["list_str", "space in elem", "3"]

conf_string = 'param_string value'

conf_string_with_comment = 'param_string value'  # comment


conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'  # comment
conf_int = 1
conf_float = 1.1
conf_list_int = [1, 2, 3]
conf_list_str = ["list_str", "space in elem", "3"]

print('conf_string: ' + str(conf_string) + ' type: ' + str(type(conf_string)))
print('conf_string_with_comment: ' + str(conf_string_with_comment) + ' type: ' + str(type(conf_string_with_comment)))
print('conf_int: ' + str(conf_int) + ' type: ' + str(type(conf_int)))
print('conf_float: ' + str(conf_float) + ' type: ' + str(type(conf_float)))
print('conf_list_int: ' + str(conf_list_int) + ' type: ' + str(type(conf_list_int)))
print('conf_list_str: ' + str(conf_list_str) + ' type: ' + str(type(conf_list_str)))

print('param_string: ' + str(param_string) + ' type: ' + str(type(param_string)))
print('param_string_with_comment: ' + str(param_string_with_comment) + ' type: ' + str(type(param_string_with_comment)))
print('param_int: ' + str(param_int) + ' type: ' + str(type(param_int)))
print('param_float: ' + str(param_float) + ' type: ' + str(type(param_float)))
print('param_list_int: ' + str(param_list_int) + ' type: ' + str(type(param_list_int)))
print('param_list_str: ' + str(param_list_str) + ' type: ' + str(type(param_list_str)))

print('var_string: ' + str(var_string) + ' type: ' + str(type(var_string)))
print('var_string_with_comment: ' + str(var_string_with_comment) + ' type: ' + str(type(var_string_with_comment)))
print('var_int: ' + str(var_int) + ' type: ' + str(type(var_int)))
print('var_float: ' + str(var_float) + ' type: ' + str(type(var_float)))
print('var_list_int: ' + str(var_list_int) + ' type: ' + str(type(var_list_int)))
print('var_list_str: ' + str(var_list_str) + ' type: ' + str(type(var_list_str)))

check = conf_string
if not isinstance(check, str):
    print('conf_string is not a string. It is a ' + str(type(check)))
    exit(1)
check = conf_string_with_comment
if not isinstance(check, str):
    print('conf_string_with_comment is not a string. It is a ' + str(type(check)))
    exit(1)
check = conf_int
if not isinstance(check, int):
    print('conf_int is not an int. It is a ' + str(type(check)))
    exit(1)
check = conf_float
if not isinstance(check, float):
    print('conf_float is not a float. It is a ' + str(type(check)))
    exit(1)
check = conf_list_int
if not isinstance(check, list):
    print('conf_list_int is not a list. It is a ' + str(type(check)))
    exit(1)
for i in conf_list_int:
    if not isinstance(i, int):
        print('conf_list_int contains a non-int value: ' + str(i))
        exit(1)
check = conf_list_str
if not isinstance(check, list):
    print('conf_list_str is not a list. It is a ' + str(type(check)))
    exit(1)
for i in conf_list_str:
    if not isinstance(i, str):
        print('conf_list_str contains a non-str value: ' + str(i))
        exit(1)

check = param_string
if not isinstance(check, str):
    print('param_string is not a string. It is a ' + str(type(check)))
    exit(1)
check = param_string_with_comment
if not isinstance(check, str):
    print('param_string_with_comment is not a string. It is a ' + str(type(check)))
    exit(1)
check = param_int
if not isinstance(check, int):
    print('param_int is not an int. It is a ' + str(type(check)))
    exit(1)
check = param_float
if not isinstance(check, float):
    print('param_float is not a float. It is a ' + str(type(check)))
    exit(1)
check = param_list_int
if not isinstance(check, list):
    print('param_list_int is not a list. It is a ' + str(type(check)))
    exit(1)
for i in param_list_int:
    if not isinstance(i, int):
        print('param_list_int contains a non-int value: ' + str(i))
        exit(1)
check = param_list_str
if not isinstance(check, list):
    print('param_list_str is not a list. It is a ' + str(type(check)))
    exit(1)
for i in param_list_str:
    if not isinstance(i, str):
        print('param_list_str contains a non-str value: ' + str(i))
        exit(1)


check = var_string
if not isinstance(check, str):
    print('var_string is not a string. It is a ' + str(type(check)))
    exit(1)
check = var_string_with_comment
if not isinstance(check, str):
    print('var_string_with_comment is not a string. It is a ' + str(type(check)))
    exit(1)
check = var_int
if not isinstance(check, int):
    print('var_int is not an int. It is a ' + str(type(check)))
    exit(1)
check = var_float
if not isinstance(check, float):
    print('var_float is not a float. It is a ' + str(type(check)))
    exit(1)
check = var_list_int
if not isinstance(check, list):
    print('var_list_int is not a list. It is a ' + str(type(check)))
    exit(1)
for i in var_list_int:
    if not isinstance(i, int):
        print('var_list_int contains a non-int value: ' + str(i))
        exit(1)
check = var_list_str
if not isinstance(check, list):
    print('var_list_str is not a list. It is a ' + str(type(check)))
    exit(1)
for i in var_list_str:
    if not isinstance(i, str):
        print('var_list_str contains a non-str value: ' + str(i))
        exit(1)
print('All vars are of the correct type')

done = 'True'
a = 0.4328648310766624

file_done = open("/tmp/done_" + id + ".json", "w")
file_done.write(json.dumps(done))
file_done.close()
