setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)
if (!requireNamespace("climwin", quietly = TRUE)) {
	install.packages("climwin", repos="http://cran.us.r-project.org")
}
library(climwin)
if (!requireNamespace("zoo", quietly = TRUE)) {
	install.packages("zoo", repos="http://cran.us.r-project.org")
}
library(zoo)

print("Retrieving input parameters")

option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--rolling_mean_temp_str"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--temperature_data_str"), action="store", default=NA, type="character", help="my description")

)
print(option_list)