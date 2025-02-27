from rasterio.merge import merge
import os
import rasterio
import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--habitat_number', action='store', type=str, required=True, dest='habitat_number')

arg_parser.add_argument('--year_paths', action='store', type=str, required=True, dest='year_paths')


args = arg_parser.parse_args()
print(args)

id = args.id

habitat_number = args.habitat_number.replace('"','')
year_paths = json.loads(args.year_paths)





def download_file_from_url(tif_url, download_path):
    """Function to download a file if it's a URL"""
    if tif_url.startswith("http"):
        response = requests.get(tif_url, stream=True)
        if response.status_code == 200:
            with open(download_path, "wb") as out_file:
                out_file.write(response.content)
        else:
            print(f"Failed to download: {tif_url}")
            return None
    else:
        return tif_url
    return download_path


def merge_tif_files(folder_path, output_filename):
    """
    Merges all GeoTIFF files in the given folder and saves the merged result.
    
    Parameters:
    - folder_path: str, path to the folder containing GeoTIFF files
    - output_filename: str, name of the output merged GeoTIFF file
    """
    tif_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.tif')]
    
    if not tif_files:
        return None
    
    src_files_to_mosaic = [rasterio.open(fp) for fp in tif_files]

    mosaic, out_transform = merge(src_files_to_mosaic)

    merged_tif_path = os.path.join(folder_path, output_filename)
    with rasterio.open(
        merged_tif_path, "w",
        driver="GTiff",
        height=mosaic.shape[1],
        width=mosaic.shape[2],
        count=src_files_to_mosaic[0].count,
        dtype=src_files_to_mosaic[0].dtypes[0],
        crs=src_files_to_mosaic[0].crs,
        transform=out_transform
    ) as dest:
        dest.write(mosaic)
    
    for src in src_files_to_mosaic:
        src.close()
    return merged_tif_path

merged_tifs = []
for year_path in year_paths:
    files_in_year_folder = [file for file in os.listdir(year_path) if file.endswith('.txt')]
    for txt_file in files_in_year_folder:
        txt_path = os.path.join(year_path, txt_file)
        print(txt_path)
        with open(txt_path, "r") as f:
            tif_paths = [line.strip() for line in f.readlines()]
        for tif_path_mean in tif_paths:
            mean_url = f"http://opendap.biodt.eu/ias-pdt/0/outputs/hab{habitat_number}/predictions/{tif_path_mean}"
            tif_filename = os.path.join(year_path, os.path.basename(mean_url))
            downloaded_file = download_file_from_url(mean_url, tif_filename)
        year = os.path.basename(year_path)
        merged_output_filename = f"{year}_merged_output.tif"
        merged_tif = merge_tif_files(year_path, merged_output_filename)
        merged_tifs.append(merged_tif)
            
        

file_merged_tifs = open("/tmp/merged_tifs_" + id + ".json", "w")
file_merged_tifs.write(json.dumps(merged_tifs))
file_merged_tifs.close()
