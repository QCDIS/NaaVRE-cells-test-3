setwd('/app')
library(optparse)
library(jsonlite)

from os.path import isfile
from os.path import join
from os import listdir
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


{'conf_data_folder': "os.path.join('/tmp','data')"}

print("Running the cell")
conf_data_folder = os.path.join('/tmp','data')

L = ["a\n", "b\n", "c\n"]
file_path =  os.path.join(conf_data_folder,'hello.txt')
fp = open(file_path, 'w')
fp.writelines(L)
fp.close()

onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)
# capturing outputs
print('Serialization of file_path')
file <- file(paste0('/tmp/file_path_', id, '.json'))
writeLines(toJSON(file_path, auto_unbox=TRUE), file)
close(file)
