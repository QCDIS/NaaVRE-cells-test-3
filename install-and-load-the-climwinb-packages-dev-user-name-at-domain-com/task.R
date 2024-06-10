setwd('/app')
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


print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")
)


opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    if (is.null(var)){
        print("Variable is null")
        exit(1)
    }
    tryCatch(
        {
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        error=function(e) {
            print("Error while deserializing the variable")
            print(var)
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        warning=function(w) {
            print("Warning while deserializing the variable")
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        }
    )
}

print("Retrieving id")
var = opt$id
print(var)
var_len = length(var)
print(paste("Variable id has length", var_len))

id <- gsub("\"", "", opt$id)


print("Running the cell")
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

a = 0.464942564753964
# capturing outputs
print('Serialization of rolling_mean_temp_str')
file <- file(paste0('/tmp/rolling_mean_temp_str_', id, '.json'))
writeLines(toJSON(rolling_mean_temp_str, auto_unbox=TRUE), file)
close(file)
print('Serialization of temperature_data_str')
file <- file(paste0('/tmp/temperature_data_str_', id, '.json'))
writeLines(toJSON(temperature_data_str, auto_unbox=TRUE), file)
close(file)
