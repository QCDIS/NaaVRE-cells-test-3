setwd('/app')
library(optparse)
library(jsonlite)



secret_float = Sys.getenv('secret_float')
secret_int = Sys.getenv('secret_int')
secret_list_int = Sys.getenv('secret_list_int')
secret_list_str = Sys.getenv('secret_list_str')
secret_string = Sys.getenv('secret_string')
secret_string_with_comment = Sys.getenv('secret_string_with_comment')

print('option_list')
option_list = list(

make_option(c("--param_float"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--param_int"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--param_list_int"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_list_str"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_string"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_string_with_comment"), action="store", default=NA, type="character", help="my description"),
make_option(c("--var_float"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--var_int"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--var_list_int"), action="store", default=NA, type="character", help="my description"),
make_option(c("--var_list_str"), action="store", default=NA, type="character", help="my description"),
make_option(c("--var_string"), action="store", default=NA, type="character", help="my description"),
make_option(c("--var_string_with_comment"), action="store", default=NA, type="character", help="my description"),
make_option(c("--id"), action="store", default=NA, type="character", help="task id")
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

print("Retrieving param_float")
var = opt$param_float
print(var)
var_len = length(var)
print(paste("Variable param_float has length", var_len))

param_float = opt$param_float
print("Retrieving param_int")
var = opt$param_int
print(var)
var_len = length(var)
print(paste("Variable param_int has length", var_len))

param_int = opt$param_int
print("Retrieving param_list_int")
var = opt$param_list_int
print(var)
var_len = length(var)
print(paste("Variable param_list_int has length", var_len))

print("------------------------Running var_serialization for param_list_int-----------------------")
print(opt$param_list_int)
param_list_int = var_serialization(opt$param_list_int)
print("---------------------------------------------------------------------------------")

print("Retrieving param_list_str")
var = opt$param_list_str
print(var)
var_len = length(var)
print(paste("Variable param_list_str has length", var_len))

print("------------------------Running var_serialization for param_list_str-----------------------")
print(opt$param_list_str)
param_list_str = var_serialization(opt$param_list_str)
print("---------------------------------------------------------------------------------")

print("Retrieving param_string")
var = opt$param_string
print(var)
var_len = length(var)
print(paste("Variable param_string has length", var_len))

param_string <- gsub("\"", "", opt$param_string)
print("Retrieving param_string_with_comment")
var = opt$param_string_with_comment
print(var)
var_len = length(var)
print(paste("Variable param_string_with_comment has length", var_len))

param_string_with_comment <- gsub("\"", "", opt$param_string_with_comment)
print("Retrieving var_float")
var = opt$var_float
print(var)
var_len = length(var)
print(paste("Variable var_float has length", var_len))

var_float = opt$var_float
print("Retrieving var_int")
var = opt$var_int
print(var)
var_len = length(var)
print(paste("Variable var_int has length", var_len))

var_int = opt$var_int
print("Retrieving var_list_int")
var = opt$var_list_int
print(var)
var_len = length(var)
print(paste("Variable var_list_int has length", var_len))

print("------------------------Running var_serialization for var_list_int-----------------------")
print(opt$var_list_int)
var_list_int = var_serialization(opt$var_list_int)
print("---------------------------------------------------------------------------------")

print("Retrieving var_list_str")
var = opt$var_list_str
print(var)
var_len = length(var)
print(paste("Variable var_list_str has length", var_len))

print("------------------------Running var_serialization for var_list_str-----------------------")
print(opt$var_list_str)
var_list_str = var_serialization(opt$var_list_str)
print("---------------------------------------------------------------------------------")

print("Retrieving var_string")
var = opt$var_string
print(var)
var_len = length(var)
print(paste("Variable var_string has length", var_len))

var_string <- gsub("\"", "", opt$var_string)
print("Retrieving var_string_with_comment")
var = opt$var_string_with_comment
print(var)
var_len = length(var)
print(paste("Variable var_string_with_comment has length", var_len))

var_string_with_comment <- gsub("\"", "", opt$var_string_with_comment)
id <- gsub('"', '', opt$id)

conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'
conf_int = 1
conf_float = 1.1
conf_list_int = list(1, 2, 3)
conf_list_str = list('list_str', 'space in elem', '3')

print("Running the cell")
print(paste('conf_string: ', conf_string, ' type: ', class(conf_string)))
print(paste('conf_string_with_comment: ', conf_string_with_comment, ' type: ', class(conf_string_with_comment)))
print(paste('conf_int: ', conf_int, ' type: ', class(conf_int)))
print(paste('conf_float: ', conf_float, ' type: ', class(conf_float)))
print(paste('conf_list_int: ', toString(conf_list_int), ' type: ', class(conf_list_int)))
print(paste('conf_list_str: ', toString(conf_list_str), ' type: ', class(conf_list_str)))

print(paste('param_string: ', param_string, ' type: ', class(param_string)))
print(paste('param_string_with_comment: ', param_string_with_comment, ' type: ', class(param_string_with_comment)))
print(paste('param_int: ', param_int, ' type: ', class(param_int)))
print(paste('param_float: ', param_float, ' type: ', class(param_float)))
print(paste('param_list_int: ', toString(param_list_int), ' type: ', class(param_list_int)))
print(paste('param_list_str: ', toString(param_list_str), ' type: ', class(param_list_str)))

print(paste('secret_string: ', secret_string, ' type: ', class(secret_string)))
print(paste('secret_string_with_comment: ', secret_string_with_comment, ' type: ', class(secret_string_with_comment)))
print(paste('secret_int: ', secret_int, ' type: ', class(secret_int)))
print(paste('secret_float: ', secret_float, ' type: ', class(secret_float)))
print(paste('secret_list_int: ', toString(secret_list_int), ' type: ', class(secret_list_int)))
print(paste('secret_list_str: ', toString(secret_list_str), ' type: ', class(secret_list_str)))

print(paste('var_string: ', var_string, ' type: ', class(var_string)))
print(paste('var_string_with_comment: ', var_string_with_comment, ' type: ', class(var_string_with_comment)))
print(paste('var_int: ', var_int, ' type: ', class(var_int)))
print(paste('var_float: ', var_float, ' type: ', class(var_float)))
print(paste('var_list_int: ', toString(var_list_int), ' type: ', class(var_list_int)))
print(paste('var_list_str: ', toString(var_list_str), ' type: ', class(var_list_str)))
