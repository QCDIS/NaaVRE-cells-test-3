setwd('/app')
library(optparse)
library(jsonlite)

{'asname': None, 'module': '', 'name': 'glob'}
{'asname': None, 'module': '', 'name': 'os'}
{'asname': None, 'module': '', 'name': 'pathlib'}



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


{'name': 'conf_local_path_split', 'assignation': "conf_local_path_split = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'split')"}

print("Running the cell")
S2_done 

split_laz_folder = glob.glob(os.path.join(conf_local_path_split, '*.LAZ'))
split_laz_files = []
print("File names ending with .LAZ:")
for file_path in split_laz_folder:
    split_laz_files.append(os.path.basename(file_path))

print(split_laz_files)
S21_done = 'True'
# capturing outputs
print('Serialization of {'name': 'split_laz_files', 'type': 'list'}')
file <- file(paste0('/tmp/{'name': 'split_laz_files', 'type': 'list'}_', id, '.json'))
writeLines(toJSON({'name': 'split_laz_files', 'type': 'list'}, auto_unbox=TRUE), file)
close(file)
