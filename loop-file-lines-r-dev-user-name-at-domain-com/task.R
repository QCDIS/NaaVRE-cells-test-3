setwd('/app')
library(optparse)
library(jsonlite)



print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--lines"), action="store", default=NA, type="character", help="my description")
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
print("Retrieving lines")
var = opt$lines
print(var)
var_len = length(var)
print(paste("Variable lines has length", var_len))

print("------------------------Running var_serialization for lines-----------------------")
print(opt$lines)
lines = var_serialization(opt$lines)
print("---------------------------------------------------------------------------------")



print("Running the cell")
count <- 0
for (l in lines) {
    count <- count + 1
    cat(sprintf("Line %d: %s\n", count, trimws(l)))
}
a = 0.6662723886790094
# capturing outputs
print('Serialization of count')
file <- file(paste0('/tmp/count_', id, '.json'))
writeLines(toJSON(count, auto_unbox=TRUE), file)
close(file)
