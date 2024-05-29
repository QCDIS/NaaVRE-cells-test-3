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






list_of_paths <- c(
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname",
  "/webdav/LAZ/targets_myname"
)

list_of_ints <- c(1, 2, 35, 6, 65)

print(list_of_paths)
print(list_of_ints)
a = 0.25365565291630066



# capturing outputs
file <- file(paste0('/tmp/list_of_paths_', id, '.json'))
writeLines(toJSON(list_of_paths, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/list_of_ints_', id, '.json'))
writeLines(toJSON(list_of_ints, auto_unbox=TRUE), file)
close(file)
