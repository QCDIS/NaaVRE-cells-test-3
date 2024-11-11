setwd('/app')
library(optparse)
library(jsonlite)

{'asname': None, 'module': '', 'name': 'os'}



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
print(a)
cmd = "KNMI_vol_h5_to_ODIM_h5 "

out = os.system(cmd)  # returns the exit code in unix
# capturing outputs
print('Serialization of {'name': 'out', 'type': 'int'}')
file <- file(paste0('/tmp/{'name': 'out', 'type': 'int'}_', id, '.json'))
writeLines(toJSON({'name': 'out', 'type': 'int'}, auto_unbox=TRUE), file)
close(file)
