setwd('/app')
library(optparse)
library(jsonlite)



print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")
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
a = 0.4863989773922468
# capturing outputs
print('Serialization of list_of_paths')
file <- file(paste0('/tmp/list_of_paths_', id, '.json'))
writeLines(toJSON(list_of_paths, auto_unbox=TRUE), file)
close(file)
print('Serialization of list_of_ints')
file <- file(paste0('/tmp/list_of_ints_', id, '.json'))
writeLines(toJSON(list_of_ints, auto_unbox=TRUE), file)
close(file)
