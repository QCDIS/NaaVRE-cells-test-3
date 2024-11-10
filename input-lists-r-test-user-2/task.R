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
list_of_paths <- c(
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname"
)

list_of_ints <- c(1, 2, 35, 6, 65)


print(list_of_paths)
print(list_of_ints)
# capturing outputs
print('Serialization of {'name': 'list_of_paths', 'type': None}')
file <- file(paste0('/tmp/{'name': 'list_of_paths', 'type': None}_', id, '.json'))
writeLines(toJSON({'name': 'list_of_paths', 'type': None}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'list_of_ints', 'type': None}')
file <- file(paste0('/tmp/{'name': 'list_of_ints', 'type': None}_', id, '.json'))
writeLines(toJSON({'name': 'list_of_ints', 'type': None}, auto_unbox=TRUE), file)
close(file)
