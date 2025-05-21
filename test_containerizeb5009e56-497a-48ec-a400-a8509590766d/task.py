import os
import pathlib
from matplotlib import pyplot
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--S6_done', action='store', type=str, required=True, dest='S6_done')


args = arg_parser.parse_args()
print(args)

id = args.id

S6_done = args.S6_done.replace('"','')


conf_local_path_geotiff = conf_local_path_geotiff = os.path.join(pathlib.Path('/tmp/data').as_posix(), 'geotiff')

S6_done

geo_tiff = os.path.join(conf_local_path_geotiff, 'geotiff_TILE_000_BAND_perc_95_normalized_height.tif')
src = rasterio.open(geo_tiff)
show(src)
fig, ax = pyplot.subplots(1, figsize=(30, 30))
show((src, 1), interpolation='none', ax=ax)
show((src, 1), contour=True, ax=ax)
pyplot.show()
show_hist(src, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
pyplot.show()

