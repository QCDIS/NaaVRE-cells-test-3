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

L <- c("a", "b", "c")

conf_data_folder <- "/tmp/data"
file_path <- file.path(conf_data_folder, "hello.txt")

writeLines(L, file_path)

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)
a = 0.07196327448468542
# capturing outputs
print('Serialization of file_path')
file <- file(paste0('/tmp/file_path_', id, '.json'))
writeLines(toJSON(file_path, auto_unbox=TRUE), file)
close(file)
