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

var = opt$count
if (is.null(var) || var == NA || var == ""){
    print("Variable opt$count is null")
    exit(1)
}

count = opt$count

var = opt$id
if (is.null(var) || var == NA || var == ""){
    print("Variable opt$id is null")
    exit(1)
}

id <- gsub("\"", "", opt$id)


print("Running the cell")

a = count + 1
a = 0.4494329508658961
