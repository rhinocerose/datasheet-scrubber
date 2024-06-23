import sys
# import pytesseract
# import statistics
import os
# import csv
# import cv2
# import concurrent.futures
# import functools
# import copy
# import numpy as np
# import argparse  # arguement parsing
#import tensorflow
from tensorflow.keras.models import load_model

pyth_dir = os.path.dirname(__file__)

root = os.path.join(pyth_dir,'Table_extract_robust')


identify_model = load_model(os.path.join(root, r"Identification_Models", "stage1.h5"))
identify_model2 = load_model(os.path.join(root, r"Identification_Models", "stage2.h5"))
valid_cells_model = load_model(os.path.join(root, "valid_cells.h5"))
conc_col_model = load_model(os.path.join(root, "conc_col.h5"))
#conc_col_model.save("conc_col_saved.h5")