setwd('/app')
library(optparse)
library(jsonlite)




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


{'name': 'conf_float', 'assignation': 'conf_float = 1.1'}
{'name': 'conf_int', 'assignation': 'conf_int = 1'}
{'name': 'conf_list_int', 'assignation': 'conf_list_int = [1, 2, 3]'}
{'name': 'conf_list_str', 'assignation': "conf_list_str = ['list_str', 'space in elem', '3']"}
{'name': 'conf_string', 'assignation': "conf_string = 'param_string value'"}
{'name': 'conf_string_with_comment', 'assignation': "conf_string_with_comment = 'param_string value'"}

print("Running the cell")
print(done)

check_string = 'param_string value'
check_string_with_comment = 'param_string value'  # comment
check_int = 1
check_float = 1.1
check_list_int = [1, 2, 3]
check_list_str = ["list_str", "space in elem", "3"]

assert conf_string == check_string
assert conf_string_with_comment == check_string_with_comment
assert conf_int == check_int
assert conf_float == check_float
assert conf_list_int == check_list_int
assert conf_list_str == check_list_str


assert param_string == check_string
assert param_string_with_comment == check_string_with_comment
assert param_int == check_int
assert param_float == check_float
assert param_list_int == check_list_int
assert param_list_str == check_list_str

print("All variables are the same.")
