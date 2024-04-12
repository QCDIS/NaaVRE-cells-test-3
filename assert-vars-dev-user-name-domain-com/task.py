
import argparse
import json
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--done', action='store', type=str, required=True, dest='done')


args = arg_parser.parse_args()
print(args)

id = args.id

done = args.done.replace('"','')


conf_string = 'param_string value'

conf_string_with_comment = 'param_string value'  # comment

conf_int = 1

conf_float = 1.1

conf_list_int = [1, 2, 3]

conf_list_str = ["list_str", "space in elem", "3"]


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

print("All variables are the same.")

