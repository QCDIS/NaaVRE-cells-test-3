setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--file_path"), action="store", default=NA, type="character", help="my description"), 
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



conf_data_folder <- file.path('/tmp', 'data')

print('-----------Running cell----------------')
conf_data_folder <- file.path('/tmp', 'data')

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)

f <- file(file_path, "r")
lines <- readLines(f)
close(f)
print('-----------Cell executed----------------')

# capturing outputs
print('Serialization of lines')
file <- file(paste0('/tmp/lines_', id, '.json'))
writeLines(toJSON(lines, auto_unbox=TRUE), file)
close(file)
