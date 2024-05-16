setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--count"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)
print("------------------Option list------------------")
print(option_list)


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

var = opt$count
var_len = length(var)
print(paste("Variable count has length", var_len))

count = opt$count

var = opt$id
var_len = length(var)
print(paste("Variable id has length", var_len))

id <- gsub("\"", "", opt$id)


print("Running the cell")

a = count + 1
