setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--list_of_paths"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving list_of_paths")
var = opt$list_of_paths
print(var)
var_len = length(var)
print(paste("Variable list_of_paths has length", var_len))

print("------------------------Running var_serialization for list_of_paths-----------------------")
print(opt$list_of_paths)
list_of_paths = var_serialization(opt$list_of_paths)
print("---------------------------------------------------------------------------------")

id <- gsub('"', '', opt$id)

{'assignation': "conf_data_folder<-'/tmp/data'", 'name': 'conf_data_folder'}

print("Running the cell")
for (l in list_of_paths) {
    print(l)
}
