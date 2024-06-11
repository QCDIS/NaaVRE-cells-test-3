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






L <- c("a", "b", "c")

conf_data_folder <- "/tmp/data"
file_path <- file.path(conf_data_folder, "hello.txt")

writeLines(L, file_path)

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)
a = 0.40655733574229436



# capturing outputs
file <- file(paste0('/tmp/file_path_', id, '.json'))
writeLines(toJSON(file_path, auto_unbox=TRUE), file)
close(file)
