setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

print("Retrieving input parameters")

option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--lines"), action="store", default=NA, type="character", help="my description")

)
print(option_list)