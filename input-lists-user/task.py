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
list_of_paths = ["/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname","/webdav/LAZ/targets_myname"]
list_of_ints = [1,2,35,6,65]
print(msg)
# capturing outputs
print('Serialization of {'name': 'list_of_ints', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'list_of_ints', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'list_of_ints', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'list_of_paths', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'list_of_paths', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'list_of_paths', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
