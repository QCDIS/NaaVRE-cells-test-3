setwd('/app')
library(optparse)
library(jsonlite)

{'asname': None, 'module': 'laserfarm', 'name': 'Retiler'}
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


{'name': 'conf_local_path_retiled', 'assignation': "conf_local_path_retiled = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'retiled')"}
{'name': 'conf_local_path_split', 'assignation': "conf_local_path_split = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'split')"}
{'name': 'conf_max_x', 'assignation': "conf_max_x = '398892.19'"}
{'name': 'conf_max_y', 'assignation': "conf_max_y = '726783.87'"}
{'name': 'conf_min_x', 'assignation': "conf_min_x = '-113107.81'"}
{'name': 'conf_min_y', 'assignation': "conf_min_y = '214783.87'"}
{'name': 'conf_n_tiles_side', 'assignation': "conf_n_tiles_side = '512'"}

print("Running the cell")
split_laz_files

grid_retile = {
    'min_x': float(conf_min_x),
    'max_x': float(conf_max_x),
    'min_y': float(conf_min_y),
    'max_y': float(conf_max_y),
    'n_tiles_side': int(conf_n_tiles_side)
}

retiling_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_split,
        'output_folder': conf_local_path_retiled
    },
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
}

for file in split_laz_files:
    clean_file = file.replace('"','').replace('[','').replace(']','')
    print(clean_file)
    retiler = Retiler(clean_file,label=clean_file).config(retiling_input)
    retiler_output = retiler.run()

S3_done = 'True'
# capturing outputs
print('Serialization of {'name': 'S3_done', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'S3_done', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'S3_done', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
