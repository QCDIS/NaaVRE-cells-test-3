import json
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_float', action='store', type=float, required=True, dest='param_float')
arg_parser.add_argument('--param_int', action='store', type=int, required=True, dest='param_int')
arg_parser.add_argument('--param_list_int', action='store', type=str, required=True, dest='param_list_int')
arg_parser.add_argument('--param_list_str', action='store', type=str, required=True, dest='param_list_str')
arg_parser.add_argument('--param_string', action='store', type=str, required=True, dest='param_string')
arg_parser.add_argument('--param_string_with_comment', action='store', type=str, required=True, dest='param_string_with_comment')

args = arg_parser.parse_args()
print(args)

id = args.id


param_float = args.param_float
param_int = args.param_int
param_list_int = json.loads(args.param_list_int)
param_list_str = json.loads(args.param_list_str)
param_string = args.param_string.replace('"','')
param_string_with_comment = args.param_string_with_comment.replace('"','')



        
print('param_string: ' + str(param_string)+' type: '+str(type(param_string)))
print('param_string_with_comment: ' + str(param_string_with_comment)+' type: '+str(type(param_string_with_comment)))
print('param_int: ' + str(param_int)+' type: '+str(type(param_int)))
print('param_float: ' + str(param_float)+' type: '+str(type(param_float)))
print('param_list_int: ' + str(param_list_int)+' type: '+str(type(param_list_int)))
print('param_list_str: ' + str(param_list_str)+' type: '+str(type(param_list_str)))


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

