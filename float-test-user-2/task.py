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
c = 2.4
# capturing outputs
print('Serialization of {'name': 'c', 'type': 'float'}')
file <- file(paste0('/tmp/{'name': 'c', 'type': 'float'}_', id, '.json'))
writeLines(toJSON({'name': 'c', 'type': 'float'}, auto_unbox=TRUE), file)
close(file)
