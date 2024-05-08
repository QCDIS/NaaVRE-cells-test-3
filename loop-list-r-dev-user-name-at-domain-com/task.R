setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--list_of_paths"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(in_var){
    tryCatch(
        {
            in_var <- fromJSON(in_var)
            return(in_var)
        },
        error=function(e) {
            in_var  <- gsub("'", '"', in_var)
            in_var  <- fromJSON(in_var)
            return(in_var)
        },
        warning=function(w) {
            in_var  <- gsub("'", '"', in_var)
            in_var  <- fromJSON(in_var)
            return(in_var)
        }
    )
}


id <- gsub('"', '', opt$id)
print('Serialization of list_of_paths')
list_of_paths = var_serialization(opt$list_of_paths)


print('-----------Running cell----------------')

for (l in list_of_paths) {
    print(l)
}
a = 0.283660873343093
print('-----------Cell executed----------------')

