setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--file_path"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving file_path")
var = opt$file_path
print(var)
var_len = length(var)
print(paste("Variable file_path has length", var_len))

file_path = opt$file_path
id <- gsub('"', '', opt$id)

{'name': 'conf_data_folder', 'assignation': 'conf_data_folder<-"/tmp/data"'}

print("Running the cell")
onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)

f <- file(file_path, "r")
lines <- readLines(f)
close(f)
# capturing outputs
print('Serialization of lines')
file <- file(paste0('/tmp/lines_', id, '.json'))
writeLines(toJSON(lines, auto_unbox=TRUE), file)
close(file)
