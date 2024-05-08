setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

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




print('-----------Running cell----------------')

L <- c("a", "b", "c")

conf_data_folder <- "/tmp/data"
file_path <- file.path(conf_data_folder, "hello.txt")

writeLines(L, file_path)

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)
print('-----------Cell executed----------------')

# capturing outputs
print('Serialization of file_path')
file <- file(paste0('/tmp/file_path_', id, '.json'))
writeLines(toJSON(file_path, auto_unbox=TRUE), file)
close(file)
