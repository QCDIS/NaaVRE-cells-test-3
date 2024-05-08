setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--lines"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(in_var){
    tryCatch(
        {
            in_var <<- fromJSON(in_var)
            return(in_var)
        },
        error=function(e) {
             <<- gsub("'", '"', in_var)
             <<- fromJSON(in_var)
            return(in_var)
        },
        warning=function(w) {
             <<- gsub("'", '"', in_var)
             <<- fromJSON(in_var)
            return(in_var)
        }
    )
}


print('Serialization of lines')
lines = var_serialization(opt$lines)



print('-----------Running cell----------------')
count <- 0
for (l in lines) {
    count <- count + 1
    cat(sprintf("Line %d: %s\n", count, trimws(l)))
}
print('-----------Cell executed----------------')

# capturing outputs
print('Serialization of count')
file <- file(paste0('/tmp/count_', id, '.json'))
writeLines(toJSON(count, auto_unbox=TRUE), file)
close(file)
