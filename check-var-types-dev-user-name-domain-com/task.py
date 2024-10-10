setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

)


opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    if (is.null(var)){
        print("Variable is null")
        exit(1)
    }
    tryCatch(
        {
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        error=function(e) {
            print("Error while deserializing the variable")
            print(var)
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        warning=function(w) {
            print("Warning while deserializing the variable")
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        }
    )
}


{'conf_float': '1.1'}
{'conf_int': '1'}
{'conf_list_int': '[1, 2, 3]'}
{'conf_list_str': '["list_str", "space in elem", "3"]'}
{'conf_string': "'param_string value'"}
{'conf_string_with_comment': "'param_string value'  # comment"}

print("Running the cell")
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
# capturing outputs
print('Serialization of done')
file <- file(paste0('/tmp/done_', id, '.json'))
writeLines(toJSON(done, auto_unbox=TRUE), file)
close(file)
