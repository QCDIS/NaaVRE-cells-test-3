setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--list_of_paths"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

id <- gsub('"', '', opt$id)
list_of_paths <- NULL
print('Serialization of list_of_paths')
tryCatch({
  list_of_paths <<- fromJSON(opt$list_of_paths)
}, error = function(e) {
  list_of_paths <<- gsub("'", '"', opt$list_of_paths)
  list_of_paths <<- fromJSON(list_of_paths)
})


print('-----------Running cell----------------')

for (l in list_of_paths) {
    print(l)
}
a = 0.2688113660220349
print('-----------Cell executed----------------')

