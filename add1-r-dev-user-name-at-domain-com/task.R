setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--count"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--id"), action="store", default=NA, type="character", help="my description")

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


count = opt$count


print('-----------Running cell----------------')

a = count + 1
print('-----------Cell executed----------------')

