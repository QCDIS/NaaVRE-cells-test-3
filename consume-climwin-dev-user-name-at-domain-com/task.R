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

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--rolling_mean_temp_str"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--temperature_data_str"), action="store", default=NA, type="character", help="my description")
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
print("Retrieving rolling_mean_temp_str")
var = opt$rolling_mean_temp_str
print(var)
var_len = length(var)
print(paste("Variable rolling_mean_temp_str has length", var_len))

rolling_mean_temp_str <- gsub("\"", "", opt$rolling_mean_temp_str)
print("Retrieving temperature_data_str")
var = opt$temperature_data_str
print(var)
var_len = length(var)
print(paste("Variable temperature_data_str has length", var_len))

temperature_data_str <- gsub("\"", "", opt$temperature_data_str)


print("Running the cell")

cat("Original Temperature Data:\n", head(temperature_data_str), "\n\n")
cat("Rolling Mean Temperature in Moving Windows:\n", head(coredata(rolling_mean_temp_str)), "\n")
a = 0.6077263799726663
