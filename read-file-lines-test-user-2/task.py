setwd('/app')
library(optparse)
library(jsonlite)

{'asname': None, 'module': 'os.path', 'name': 'isfile'}
{'asname': None, 'module': 'os.path', 'name': 'join'}
{'asname': None, 'module': 'os', 'name': 'listdir'}
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


{'name': 'conf_data_folder', 'assignation': "conf_data_folder = os.path.join('/tmp', 'data')"}

print("Running the cell")
onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)

f = open(file_path, 'r')
lines = f.readlines()
f.close()
# capturing outputs
print('Serialization of {'name': 'lines', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'lines', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'lines', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
