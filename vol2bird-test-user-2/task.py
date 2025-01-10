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
cmd = "vol2bird --version"

msg = os.system(cmd)  # returns the exit code in unix
# capturing outputs
print('Serialization of {'name': 'msg', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'msg', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'msg', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
