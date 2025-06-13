import matplotlib.pyplot as plt
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




np.random.random()
fig, ax = plt.subplots(figsize=(10, 8))

