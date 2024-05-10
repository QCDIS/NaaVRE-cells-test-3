setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)
if (!requireNamespace("jsonlite", quietly = TRUE)) {
	install.packages("jsonlite", repos="http://cran.us.r-project.org")
}
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    tryCatch(
        {
            var <- fromJSON(var)
            return(var)
        },
        error=function(e) {
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            return(var)
        },
        warning=function(w) {
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            return(var)
        }
    )
}

id <- gsub("\"", "", opt$id)



var_string <- 'var_string value'
var_string_with_comment <- 'var_string value'  # comment
var_int <- 1
var_float <- 1.1
var_list_int <- list(1, 2, 3)
var_list_str <- list("list_str", "space in elem", "3")
print(class(var_list_int))
# capturing outputs
print('Serialization of var_string')
file <- file(paste0('/tmp/var_string_', id, '.json'))
writeLines(toJSON(var_string, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_string_with_comment')
file <- file(paste0('/tmp/var_string_with_comment_', id, '.json'))
writeLines(toJSON(var_string_with_comment, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_int')
file <- file(paste0('/tmp/var_int_', id, '.json'))
writeLines(toJSON(var_int, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_float')
file <- file(paste0('/tmp/var_float_', id, '.json'))
writeLines(toJSON(var_float, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_list_int')
file <- file(paste0('/tmp/var_list_int_', id, '.json'))
writeLines(toJSON(var_list_int, auto_unbox=TRUE), file)
close(file)
print('Serialization of var_list_str')
file <- file(paste0('/tmp/var_list_str_', id, '.json'))
writeLines(toJSON(var_list_str, auto_unbox=TRUE), file)
close(file)
