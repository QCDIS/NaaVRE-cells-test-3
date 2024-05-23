
import argparse
import json
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--done', action='store', type=str, required=True, dest='done')

arg_parser.add_argument('--param_float', action='store', type=float, required=True, dest='param_float')
arg_parser.add_argument('--param_int', action='store', type=int, required=True, dest='param_int')
arg_parser.add_argument('--param_list_int', action='store', type=str, required=True, dest='param_list_int')
arg_parser.add_argument('--param_list_str', action='store', type=str, required=True, dest='param_list_str')
arg_parser.add_argument('--param_string', action='store', type=str, required=True, dest='param_string')
arg_parser.add_argument('--param_string_with_comment', action='store', type=str, required=True, dest='param_string_with_comment')

args = arg_parser.parse_args()
print(args)

id = args.id

done = args.done.replace('"','')

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
print(done)

check_string = 'param_string value'
check_string_with_comment = 'param_string value'  # comment
check_int = 1
check_float = 1.1
check_list_int = [1, 2, 3]
check_list_str = ["list_str", "space in elem", "3"]

assert conf_string == check_string
assert conf_string_with_comment == check_string_with_comment
assert conf_int == check_int
assert conf_float == check_float
assert conf_list_int == check_list_int
assert conf_list_str == check_list_str


assert param_string == check_string
assert param_string_with_comment == check_string_with_comment
assert param_int == check_int
assert param_float == check_float
assert param_list_int == check_list_int
assert param_list_str == check_list_str

print("All variables are the same.")
a = 0.4121993422347243

