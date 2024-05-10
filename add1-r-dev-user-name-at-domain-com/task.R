setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

print("Retrieving input parameters")

option_list = list(

make_option(c("--count"), action="store", default=NA, type="integer", help="my description"), 
make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)
print(option_list)