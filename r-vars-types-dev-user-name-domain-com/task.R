setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_float"), action="store", default=NA, type="numeric", help="my description"), 
make_option(c("--param_int"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--param_list_int"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_list_str"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_string"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_string_with_comment"), action="store", default=NA, type="character", help="my description")

)

print(option_list)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

id <- gsub('"', '', opt$id)

param_float = opt$param_float
param_int = opt$param_int
tryCatch({
  param_list_int <- fromJSON(param_list_int)
}, error = function(e) {
  if (class(e) == 'jsonlite_error') {
    param_list_int <- gsub("\\[", '["', param_list_int)
    param_list_int <- gsub(",", '","', param_list_int)
    param_list_int <- gsub("\" ", "\"", param_list_int)
    param_list_int <- gsub("\\]", '"]', param_list_int)
    param_list_int <- gsub("'", "", param_list_int)
    param_list_int <- fromJSON(param_list_int)
  } else {
    stop(e)
  }
})
tryCatch({
  param_list_str <- fromJSON(param_list_str)
}, error = function(e) {
  if (class(e) == 'jsonlite_error') {
    param_list_str <- gsub("\\[", '["', param_list_str)
    param_list_str <- gsub(",", '","', param_list_str)
    param_list_str <- gsub("\" ", "\"", param_list_str)
    param_list_str <- gsub("\\]", '"]', param_list_str)
    param_list_str <- gsub("'", "", param_list_str)
    param_list_str <- fromJSON(param_list_str)
  } else {
    stop(e)
  }
})
param_string <- gsub('"', '', opt$param_string)
param_string_with_comment <- gsub('"', '', opt$param_string_with_comment)


conf_float = 1.1
conf_int = 1
conf_list_int = [1, 2, 3]
conf_list_str = ['list_str', 'space in elem', '3']
conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'


conf_string = 'param_string value'
conf_string_with_comment = 'param_string value'
conf_int = 1
conf_float = 1.1
conf_list_int = [1, 2, 3]
conf_list_str = ['list_str', 'space in elem', '3']

conf_string <- 'param_string value'
conf_string_with_comment <- 'param_string value'  # comment
conf_int <- 1
conf_float <- 1.1
conf_list_int <- c(1, 2, 3)
conf_list_str <- c("list_str", "space in elem", "3")

var_string <- 'var_string value'
var_string_with_comment <- 'var_string value'  # comment
var_int <- 1
var_float <- 1.1
var_list_int <- c(1, 2, 3)
var_list_str <- c("list_str", "space in elem", "3")



# capturing outputs
file <- file(paste0('/tmp/var_string_', id, '.json'))
writeLines(toJSON(var_string, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/var_string_with_comment_', id, '.json'))
writeLines(toJSON(var_string_with_comment, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/var_int_', id, '.json'))
writeLines(toJSON(var_int, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/var_float_', id, '.json'))
writeLines(toJSON(var_float, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/var_list_int_', id, '.json'))
writeLines(toJSON(var_list_int, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/var_list_str_', id, '.json'))
writeLines(toJSON(var_list_str, auto_unbox=TRUE), file)
close(file)
