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


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

id <- gsub('"', '', opt$id)





if (!requireNamespace("climwin", quietly = TRUE)) {
  install.packages("climwin",repos = "http://cran.us.r-project.org")
}
if (!requireNamespace("zoo", quietly = TRUE)) {
  install.packages("zoo",repos = "http://cran.us.r-project.org")
}

zoo = ''
climwin = ''
library(climwin)
library(zoo)

set.seed(123)
temperature_data <- rnorm(365, mean = 15, sd = 5)

window_size <- 30

temperature_zoo <- zoo::zoo(temperature_data)

rolling_mean_temp <- rollmean(temperature_zoo, k = window_size, fill = 0.0)

temperature_zoo_str <- toString(temperature_zoo)
rolling_mean_temp_str <- toString(rolling_mean_temp)
temperature_data_str <- toString(temperature_data)

a = 0.4064203048482957



# capturing outputs
file <- file(paste0('/tmp/rolling_mean_temp_str_', id, '.json'))
writeLines(toJSON(rolling_mean_temp_str, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/temperature_data_str_', id, '.json'))
writeLines(toJSON(temperature_data_str, auto_unbox=TRUE), file)
close(file)
