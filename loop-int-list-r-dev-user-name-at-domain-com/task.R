setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--list_of_ints"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))

id <- gsub('"', '', opt$id)
list_of_ints <- NULL
print('Serialization of list_of_ints')
tryCatch({
  list_of_ints <<- fromJSON(opt$list_of_ints)
}, error = function(e) {
  list_of_ints <<- gsub("'", '"', opt$list_of_ints)
  list_of_ints <<- fromJSON(list_of_ints)
})


print('-----------Running cell----------------')

for (l in list_of_ints) {
    print(l)
}
print('-----------Cell executed----------------')

