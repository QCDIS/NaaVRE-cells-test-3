setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)
if (!requireNamespace("numpy as np", quietly = TRUE)) {
	install.packages("numpy as np", repos="http://cran.us.r-project.org")
}
library(numpy as np)


option_list = list(

make_option(c("--a"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--b"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--c"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_h"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_i"), action="store", default=NA, type="numeric", help="my description"), 
make_option(c("--param_j"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_k"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

a = opt$a
b <- gsub('"', '', opt$b)
c = opt$c
id <- gsub('"', '', opt$id)

param_h = opt$param_h
param_i = opt$param_i
param_j = opt$param_j
param_k = opt$param_k


conf_l = 1


conf_l = 1
print(param_string)
print(param_string_with_comment)
print(param_int)
print(param_float)



# capturing outputs
file <- file(paste0('/tmp/e_', id, '.json'))
writeLines(toJSON(e, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/f_', id, '.json'))
writeLines(toJSON(f, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/g_', id, '.json'))
writeLines(toJSON(g, auto_unbox=TRUE), file)
close(file)
