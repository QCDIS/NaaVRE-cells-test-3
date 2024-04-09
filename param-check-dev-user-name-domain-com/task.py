
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_float', action='store', type=float, required=True, dest='param_float')
arg_parser.add_argument('--param_int', action='store', type=int, required=True, dest='param_int')
arg_parser.add_argument('--param_list_int', action='store', type=list, required=True, dest='param_list_int')
arg_parser.add_argument('--param_list_str', action='store', type=list, required=True, dest='param_list_str')
arg_parser.add_argument('--param_string', action='store', type=str, required=True, dest='param_string')
arg_parser.add_argument('--param_string_with_comment', action='store', type=str, required=True, dest='param_string_with_comment')

args = arg_parser.parse_args()
print(args)

id = args.id


param_float = args.param_float
param_int = args.param_int
param_list_int = args.param_list_int
param_list_str = args.param_list_str
param_string = args.param_string
param_string_with_comment = args.param_string_with_comment


print('param_string:'+ param_string)
print('param_string_with_comment: '+ param_string_with_comment)
print('param_int: '+ str(param_int))
print('param_float: '+str(param_float))
print('param_list_int: '+str(param_list_int))
print('param_list_str: '+ str(param_list_str))

