setwd('/app')
library(optparse)
library(jsonlite)

{'asname': None, 'module': 'laserfarm', 'name': 'GeotiffWriter'}
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


{'name': 'conf_local_path_geotiff', 'assignation': "conf_local_path_geotiff = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'geotiff')"}
{'name': 'conf_local_path_targets', 'assignation': "conf_local_path_targets = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'targets')"}
{'name': 'conf_feature_name', 'assignation': "conf_feature_name = 'perc_95_normalized_height'"}
{'name': 'conf_remote_path_geotiffs', 'assignation': "conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' + '' + '/geotiffs')"}
{'name': 'conf_wd_opts', 'assignation': "conf_wd_opts = {'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}"}

print("Running the cell")
S5_done

geotiff_export_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_targets,
         'output_folder': conf_local_path_geotiff
        },
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': conf_remote_path_geotiffs.as_posix(),
}

writer = GeotiffWriter(input_dir=conf_feature_name, bands=conf_feature_name, label=conf_feature_name).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

remote_path_geotiffs = str(conf_remote_path_geotiffs)
S6_done = 'True'
# capturing outputs
print('Serialization of {'name': 'S6_done', 'type': 'str'}')
file <- file(paste0('/tmp/{'name': 'S6_done', 'type': 'str'}_', id, '.json'))
writeLines(toJSON({'name': 'S6_done', 'type': 'str'}, auto_unbox=TRUE), file)
close(file)
