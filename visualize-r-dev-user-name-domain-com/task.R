setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("ggplot2", quietly = TRUE)) {
	install.packages("ggplot2", repos="http://cran.us.r-project.org")
}
library(ggplot2)


print('option_list')
option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description")
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

print("Retrieving id")
var = opt$id
print(var)
var_len = length(var)
print(paste("Variable id has length", var_len))

id <- gsub("\"", "", opt$id)


print("Running the cell")
install.packages("ggplot2")

library(ggplot2)


x = 0
y = 0
set.seed(123) # for reproducibility
data <- data.frame(
  x = rnorm(100),  # 100 random points for x-axis
  y = rnorm(100)   # 100 random points for y-axis
)

plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Scatter Plot of Random Data",
       x = "X-Axis",
       y = "Y-Axis")

ggsave("scatter_plot.png", plot)

print(plot)
# capturing outputs
print('Serialization of x')
file <- file(paste0('/tmp/x_', id, '.json'))
writeLines(toJSON(x, auto_unbox=TRUE), file)
close(file)
