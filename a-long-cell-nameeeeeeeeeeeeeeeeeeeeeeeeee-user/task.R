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
a_long_variable_nameeeeeeeeeeeeeeeee = 1
b = 1.1
c = "d"
d = list(1, 2, 3)
e = NaN
# capturing outputs
print('Serialization of {'name': 'a_long_variable_nameeeeeeeeeeeeeeeee', 'type': 'int'}')
file <- file(paste0('/tmp/{'name': 'a_long_variable_nameeeeeeeeeeeeeeeee', 'type': 'int'}_', id, '.json'))
writeLines(toJSON({'name': 'a_long_variable_nameeeeeeeeeeeeeeeee', 'type': 'int'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'b', 'type': 'float'}')
file <- file(paste0('/tmp/{'name': 'b', 'type': 'float'}_', id, '.json'))
writeLines(toJSON({'name': 'b', 'type': 'float'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'c', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'c', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'c', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
print('Serialization of {'name': 'd', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'd', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'd', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
