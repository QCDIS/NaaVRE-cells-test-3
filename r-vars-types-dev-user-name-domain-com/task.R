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

make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)
print(option_list)