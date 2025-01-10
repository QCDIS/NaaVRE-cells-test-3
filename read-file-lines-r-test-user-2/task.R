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


{'name': 'conf_data_folder', 'assignation': 'conf_data_folder<-"/tmp/data"'}

print("Running the cell")
onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)

f <- file(file_path, "r")
lines <- readLines(f)
close(f)
# capturing outputs
print('Serialization of {'name': 'lines', 'type': None}')
file <- file(paste0('/tmp/{'name': 'lines', 'type': None}_', id, '.json'))
writeLines(toJSON({'name': 'lines', 'type': None}, auto_unbox=TRUE), file)
close(file)
