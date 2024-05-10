setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)
if (!requireNamespace("jsonlite", quietly = TRUE)) {
	install.packages("jsonlite", repos="http://cran.us.r-project.org")
}
library(jsonlite)

print("Retrieving input parameters")

option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_float"), action="store", default=NA, type="numeric", help="my description"), 
make_option(c("--param_int"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--param_list_int"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_list_str"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_string"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_string_with_comment"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--var_float"), action="store", default=NA, type="numeric", help="my description"), 
make_option(c("--var_int"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--var_list_int"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--var_list_str"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--var_string"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--var_string_with_comment"), action="store", default=NA, type="character", help="my description")

)
print(option_list)