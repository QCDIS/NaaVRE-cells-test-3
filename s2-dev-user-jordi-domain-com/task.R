setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

id <- gsub('"', '', opt$id)





b = 20



# capturing outputs
file <- file(paste0('/tmp/b_', id, '.json'))
writeLines(toJSON(b, auto_unbox=TRUE), file)
close(file)
