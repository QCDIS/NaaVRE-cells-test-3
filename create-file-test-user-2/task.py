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
L = ["a\n", "b\n", "c\n"]
file_path =  os.path.join(conf_data_folder,'hello.txt')
fp = open(file_path, 'w')
fp.writelines(L)
fp.close()

onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)
# capturing outputs
print('Serialization of {'name': 'file_path', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'file_path', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'file_path', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
