setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("SecretsProvider", quietly = TRUE)) {
	install.packages("SecretsProvider", repos="http://cran.us.r-project.org")
}
library(SecretsProvider)


print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_number"), action="store", default=NA, type="integer", help="my description")
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

print("Retrieving id")
var = opt$id
print(var)
var_len = length(var)
print(paste("Variable id has length", var_len))

id <- gsub("\"", "", opt$id)
print("Retrieving param_number")
var = opt$param_number
print(var)
var_len = length(var)
print(paste("Variable param_number has length", var_len))

param_number = opt$param_number


print("Running the cell")
library(SecretsProvider)
print(param_number)
a = 0.6790948802373077
