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

file_path <- gsub('"', '', opt$file_path)
id <- gsub('"', '', opt$id)



conf_data_folder <- file.path('/tmp', 'data')


conf_data_folder <- file.path('/tmp', 'data')

onlyfiles <- list.files(conf_data_folder, full.names = TRUE)

print(onlyfiles)

f <- file(file_path, "r")
lines <- readLines(f)
close(f)
a = 0.8149806592603137



# capturing outputs
file <- file(paste0('/tmp/lines_', id, '.json'))
writeLines(toJSON(lines, auto_unbox=TRUE), file)
close(file)
