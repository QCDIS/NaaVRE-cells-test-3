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



print("Running the cell")
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
# capturing outputs
print('Serialization of {'name': 'var_string', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'var_string', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'var_string', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'var_string_with_comment', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'var_string_with_comment', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'var_string_with_comment', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'var_int', 'type': 'int'}')
file <- file(paste0('/tmp/{'name': 'var_int', 'type': 'int'}_', id, '.json'))
writeLines(toJSON({'name': 'var_int', 'type': 'int'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'var_float', 'type': 'float'}')
file <- file(paste0('/tmp/{'name': 'var_float', 'type': 'float'}_', id, '.json'))
writeLines(toJSON({'name': 'var_float', 'type': 'float'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'var_list_int', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'var_list_int', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'var_list_int', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'var_list_str', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'var_list_str', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'var_list_str', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
