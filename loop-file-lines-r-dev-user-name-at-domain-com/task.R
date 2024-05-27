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

id <- gsub('"', '', opt$id)
lines = fromJSON(opt$lines)





count <- 0
for (l in lines) {
    count <- count + 1
    cat(sprintf("Line %d: %s\n", count, trimws(l)))
}
a = 0.9858725875919426



# capturing outputs
file <- file(paste0('/tmp/count_', id, '.json'))
writeLines(toJSON(count, auto_unbox=TRUE), file)
close(file)
