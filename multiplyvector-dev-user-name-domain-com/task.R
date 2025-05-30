setwd('/app')
library(optparse)
library(jsonlite)

{'asname': '', 'module': '', 'name': 'Rcpp'}
{'asname': '', 'module': '', 'name': 'httr'}
{'asname': '', 'module': '', 'name': 'jsonlite'}
{'asname': '', 'module': '', 'name': 'readr'}



print('option_list')
option_list = list(

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



print("Running the cell")
# multiplyvector
# ----- Libraries needed for auto-generated code ----- #
library(jsonlite)
library(httr)
library(readr)
# ----- End of libraries ----- #

v1 <- 1:500000
v2 <- 500000:1

print("Created vectors")
start_run_time <- Sys.time()

library(Rcpp)

# sourceCpp("multiply_vector.cpp")

start_func_time <- Sys.time()
# result <- multiply_vectors(v1, v2)
# ----- THIS CODE IS AUTO-GENERATED BY MULTICONTAINERIZER ----- #
{# Convert each param to JSON format
json_v1 <- toJSON(as.vector(v1))
json_v2 <- toJSON(as.vector(v2))

# Prepare a list for JSON conversion
list_result <- list(
	v1 = json_v1,
	v2 = json_v2
)
# Convert to JSON format
json_result <- toJSON(list_result, auto_unbox=TRUE)
# URL dependent on configuration
url_result <- "http://localhost:8080/multiply_vectors"

# Call the correct API endpoint for this function and process the result
response_result <- POST(
	url_result,
	body = json_result,
	encode = "raw",
	add_headers("Content-Type" = "application/json")
)

content_result <- content(response_result)

# Capture the results in the original variable, and convert into correct format
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
print('Serialization of {'name': 'run_time', 'type': 'float'}')
file <- file(paste0('/tmp/{'name': 'run_time', 'type': 'float'}_', id, '.json'))
writeLines(toJSON({'name': 'run_time', 'type': 'float'}, auto_unbox=TRUE), file)
close(file)
