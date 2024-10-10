setwd('/app')
library(optparse)
library(jsonlite)

import jsonlite



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
{'conf_list_int': 'list(1, 2, 3)'}
{'conf_list_str': "list('list_str', 'space in elem', '3')"}
{'conf_string': "'param_string value'"}
{'conf_string_with_comment': "'param_string value'"}

print("Running the cell")
conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'
conf_int = 1
conf_float = 1.1
conf_list_int = list(1, 2, 3)
conf_list_str = list('list_str', 'space in elem', '3')


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

print(paste('var_string: ', var_string, ' type: ', class(var_string)))
print(paste('var_string_with_comment: ', var_string_with_comment, ' type: ', class(var_string_with_comment)))
print(paste('var_int: ', var_int, ' type: ', class(var_int)))
print(paste('var_float: ', var_float, ' type: ', class(var_float)))
print(paste('var_list_int: ', toString(var_list_int), ' type: ', class(var_list_int)))
print(paste('var_list_str: ', toString(var_list_str), ' type: ', class(var_list_str)))

check_type <- function(var, expected_types) {
  
  if (!any(sapply(expected_types, function(x) inherits(var, x)))) {
    stop(paste('Variable is not of the expected types:', paste(expected_types, collapse = ', '),
               '. It is a', class(var)))
  }
  
  if ('list' %in% expected_types) {
    if (!is.list(var) && !is.vector(var)) {
      stop(paste('Variable', var, 'is not iterable.'))
    }
  }
}

check_type(conf_string, c(c("character")))
check_type(conf_string_with_comment, c("character"))
check_type(conf_int, "numeric")
check_type(conf_float, "numeric")
if (is.numeric(conf_list_int)) {
  conf_list_int <- list(conf_list_int)
}

check_type(conf_list_int, c("list"))
if (is.character(conf_list_str)) {
  conf_list_str <- list(conf_list_str)
}
check_type(conf_list_str, c("list"))

check_type(param_string, c("character"))
check_type(param_string_with_comment, c("character"))
check_type(param_int, c("numeric", "integer"))
check_type(param_float, c("numeric", "float"))
if (is.numeric(param_list_int)) {
  param_list_int <- list(param_list_int)
}
check_type(param_list_int, c("list"))
check_type(conf_list_int, c("list"))
if (is.character(param_list_str)) {
  param_list_str <- list(param_list_str)
}
check_type(param_list_str, c("list"))

check_type(var_string, c("character"))
check_type(var_string_with_comment, c("character"))
check_type(var_int, c("numeric", "integer"))
check_type(var_float, c("numeric", "float"))
if (is.numeric(var_list_int)) {
  var_list_int <- list(var_list_int)
}
check_type(var_list_int, c("list"))

if (is.character(var_list_str)) {
  var_list_str <- list(var_list_str)
}
check_type(var_list_str, c("list"))

print('All vars are of the correct type')

done <- TRUE
