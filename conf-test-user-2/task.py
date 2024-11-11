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
conf_data_folder = os.path.join('/tmp','data')

conf_feature_name = 'perc_95_normalized_height'
conf_validate_precision = '0.001'
conf_tile_mesh_size = '10.'
conf_filter_type= 'select_equal'
conf_attribute = 'raw_classification'
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_apply_filter_value = '1'
conf_laz_compression_factor = '7'
conf_max_filesize = '262144000'  # desired max file size (in bytes)
