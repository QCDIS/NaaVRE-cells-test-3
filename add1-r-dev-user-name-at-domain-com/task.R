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

count = opt$count
id <- gsub('"', '', opt$id)






a = count + 1
a = 0.3654720213203946



