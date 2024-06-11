setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--a"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--b"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

a = opt$a
b = opt$b
id <- gsub('"', '', opt$id)





answer = a + b



