setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("Rcpp", quietly = TRUE)) {
	install.packages("Rcpp", repos="http://cran.us.r-project.org")
}
library(Rcpp)
if (!requireNamespace("httr", quietly = TRUE)) {
	install.packages("httr", repos="http://cran.us.r-project.org")
}
library(httr)
if (!requireNamespace("jsonlite", quietly = TRUE)) {
	install.packages("jsonlite", repos="http://cran.us.r-project.org")
}
library(jsonlite)
if (!requireNamespace("readr", quietly = TRUE)) {
	install.packages("readr", repos="http://cran.us.r-project.org")
}
library(readr)


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
library(jsonlite)
library(httr)
library(readr)

v1 <- 1:500000
v2 <- 500000:1

print("Created vectors")
start_run_time <- Sys.time()

library(Rcpp)


start_func_time <- Sys.time()
{# Convert each param to JSON format
json_v1 <- toJSON(as.vector(v1))
json_v2 <- toJSON(as.vector(v2))

list_result <- list(
	v1 = json_v1,
	v2 = json_v2
)
json_result <- toJSON(list_result, auto_unbox=TRUE)
url_result <- "http://localhost:8080/multiply_vectors"

response_result <- POST(
	url_result,
	body = json_result,
	encode = "raw",
	add_headers("Content-Type" = "application/json")
)

content_result <- content(response_result)

result <- as.vector(content_result)
result <- as.vector(as.numeric(result))
}# ---- END OF AUTO-GENERATED CODE ----- #
end_func_time <- Sys.time()

end_run_time <- Sys.time()

run_time <- as.numeric(end_run_time - start_run_time, units = "secs")
func_time <- as.numeric(end_func_time - start_func_time, units = "secs")

print(paste("Run time: ", run_time))
print(paste("Func time: ", func_time))
# capturing outputs
print('Serialization of run_time')
file <- file(paste0('/tmp/run_time_', id, '.json'))
writeLines(toJSON(run_time, auto_unbox=TRUE), file)
close(file)
