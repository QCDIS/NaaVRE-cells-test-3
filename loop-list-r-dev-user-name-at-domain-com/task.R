setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--list_of_paths"), action="store", default=NA, type="character", help="my description")

)
print("------------------Option list------------------")
print(option_list)


# set input parameters accordingly
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

var = opt$id
var_len = length(var)
print(paste("Variable id has length", var_len))

id <- gsub("\"", "", opt$id)

var = opt$list_of_paths
var_len = length(var)
print(paste("Variable list_of_paths has length", var_len))

print("------------------------Running var_serialization for list_of_paths-----------------------")
print(opt$list_of_paths)
list_of_paths = var_serialization(opt$list_of_paths)
print("---------------------------------------------------------------------------------")



print("Running the cell")

for (l in list_of_paths) {
    print(l)
}
a = 0.8209482516503049
