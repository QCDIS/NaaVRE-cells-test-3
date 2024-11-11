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
param_string <- 'param_string value'
param_string_with_comment <- 'param_string value'  # comment
param_int <- 1
param_float <- 1.1
param_list_int <- list(1, 2, 3)
param_list_str <- list("list_str", "space in elem", "3")

conf_string <- 'param_string value'
conf_string_with_comment <- 'param_string value'  # comment
conf_int <- 1
conf_float <- 1.1
conf_list_int <- list(1, 2, 3)
conf_list_str <- list("list_str", "space in elem", "3")
