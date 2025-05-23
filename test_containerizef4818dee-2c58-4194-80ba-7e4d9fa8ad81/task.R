setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

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

id <- gsub('"', '', opt$id)

{'assignation': 'conf_float<-1.1', 'name': 'conf_float'}
{'assignation': 'conf_int<-1', 'name': 'conf_int'}
{'assignation': 'conf_list_int <- list(1, 2, 3)', 'name': 'conf_list_int'}
{'assignation': 'conf_list_str <- list("list_str", "space in elem", "3")', 'name': 'conf_list_str'}
{'assignation': "conf_string<-'param_string value'", 'name': 'conf_string'}
{'assignation': "conf_string_with_comment<-'param_string value'", 'name': 'conf_string_with_comment'}

print("Running the cell")
var_string <- 'var_string value'
var_string_with_comment <- 'var_string value'  # comment
var_int <- 1
var_float <- 1.1
var_list_int <- list(1, 2, 3)
var_list_str <- list("list_str", "space in elem", "3")
print(class(var_list_int))
# capturing outputs
print('Serialization of var_string_with_comment')
file <- file(paste0('/tmp/var_string_with_comment_', id, '.json'))
writeLines(toJSON(var_string_with_comment, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_string')
file <- file(paste0('/tmp/var_string_', id, '.json'))
writeLines(toJSON(var_string, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_int')
file <- file(paste0('/tmp/var_int_', id, '.json'))
writeLines(toJSON(var_int, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_float')
file <- file(paste0('/tmp/var_float_', id, '.json'))
writeLines(toJSON(var_float, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_list_int')
file <- file(paste0('/tmp/var_list_int_', id, '.json'))
writeLines(toJSON(var_list_int, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_list_str')
file <- file(paste0('/tmp/var_list_str_', id, '.json'))
writeLines(toJSON(var_list_str, auto_unbox=TRUE), file)
close(file)
