setwd('/app')
library(optparse)
library(jsonlite)

import os



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
print(a)
cmd = "vol2bird --version"

msg = os.system(cmd)  # returns the exit code in unix
# capturing outputs
print('Serialization of msg')
file <- file(paste0('/tmp/msg_', id, '.json'))
writeLines(toJSON(msg, auto_unbox=TRUE), file)
close(file)
