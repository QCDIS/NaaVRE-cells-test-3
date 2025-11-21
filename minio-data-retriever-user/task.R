setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("SecretsProvider", quietly = TRUE)) {
	install.packages("SecretsProvider", repos="http://cran.us.r-project.org")
}
library(SecretsProvider)
if (!requireNamespace("aws.s3", quietly = TRUE)) {
	install.packages("aws.s3", repos="http://cran.us.r-project.org")
}
library(aws.s3)
if (!requireNamespace("readxl", quietly = TRUE)) {
	install.packages("readxl", repos="http://cran.us.r-project.org")
}
library(readxl)


secret_minio_access_key = Sys.getenv('secret_minio_access_key')
secret_minio_secret_key = Sys.getenv('secret_minio_secret_key')

print('option_list')
option_list = list(

make_option(c("--param_data_filename"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_data_sheet"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_metadata_sheet"), action="store", default=NA, type="character", help="my description"),
make_option(c("--param_use_dummy_data"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--param_user_email"), action="store", default=NA, type="character", help="my description"),
make_option(c("--id"), action="store", default=NA, type="character", help="task id")
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

print("Retrieving param_data_filename")
var = opt$param_data_filename
print(var)
var_len = length(var)
print(paste("Variable param_data_filename has length", var_len))

param_data_filename <- gsub("\"", "", opt$param_data_filename)
print("Retrieving param_data_sheet")
var = opt$param_data_sheet
print(var)
var_len = length(var)
print(paste("Variable param_data_sheet has length", var_len))

param_data_sheet <- gsub("\"", "", opt$param_data_sheet)
print("Retrieving param_metadata_sheet")
var = opt$param_metadata_sheet
print(var)
var_len = length(var)
print(paste("Variable param_metadata_sheet has length", var_len))

param_metadata_sheet <- gsub("\"", "", opt$param_metadata_sheet)
print("Retrieving param_use_dummy_data")
var = opt$param_use_dummy_data
print(var)
var_len = length(var)
print(paste("Variable param_use_dummy_data has length", var_len))

param_use_dummy_data = opt$param_use_dummy_data
print("Retrieving param_user_email")
var = opt$param_user_email
print(var)
var_len = length(var)
print(paste("Variable param_user_email has length", var_len))

param_user_email <- gsub("\"", "", opt$param_user_email)
id <- gsub('"', '', opt$id)

conf_minio_region<-"nl-uvalight"
conf_minio_endpoint<-"scruffy.lab.uvalight.net:9000"
conf_minio_user_bucket<-"naa-vre-user-data"
conf_temporary_data_directory<-"/tmp/data"
conf_minio_public_bucket<-"naa-vre-public"
conf_virtual_lab_biotisan_euromarec<-"vl-biotisan-euromarec"

print("Running the cell")
library("readxl")
library("aws.s3")

Sys.setenv("AWS_S3_ENDPOINT" = conf_minio_endpoint,
           "AWS_DEFAULT_REGION" = conf_minio_region,
           "AWS_ACCESS_KEY_ID" = secret_minio_access_key,
           "AWS_SECRET_ACCESS_KEY" = secret_minio_secret_key)

if (param_use_dummy_data) {
        file_path <- paste(conf_virtual_lab_biotisan_euromarec, param_data_filename, sep="/")
        print(sprintf("Using dummy data for testing purposes. Set param_use_dummy_data to 0 to use your own data. Downloading data from %s / %s", conf_minio_public_bucket, file_path))
        aws.s3::save_object(bucket=conf_minio_public_bucket, object=file_path, file=param_data_filename)
    } else {
        file_path <- paste(param_user_email, param_data_filename, sep="/")
        print(sprintf("Downloading data from %s / %s", conf_minio_user_bucket, file_path))
        aws.s3::save_object(bucket=conf_minio_user_bucket, object=file_path, file=param_data_filename)
}

metadata <- read_excel(param_data_filename, sheet = param_metadata_sheet) #Load metadata sheet
data <- read_excel(param_data_filename, sheet = param_data_sheet) #Load data sheet

dir.create(conf_temporary_data_directory, showWarnings = FALSE)

metadata_as_csv_filename <- "metadata.csv"
data_as_csv_filename <- "data.csv"
metadata_from_excel_path <- paste(conf_temporary_data_directory, metadata_as_csv_filename, sep="/")
data_from_excel_path <- paste(conf_temporary_data_directory, data_as_csv_filename, sep="/")
print(sprintf("Storing metadata in: %s, and data in %s", metadata_from_excel_path, data_from_excel_path))
write.csv(metadata, file = metadata_from_excel_path)
write.csv(data, file =  data_from_excel_path)
