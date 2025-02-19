#!/usr/bin/env python
import matplotlib.pyplot as plt 
import numpy as np
import os
import pandas as pd
import seaborn as sns
from tqdm import tqdm


def pickle_that(obj, fp):

    with open(fp, 'wb') as out_handle:
        pickle.dump(obj, out_handle)


def unpickle_that(fp):

    with open(fp, 'rb') as in_handle:
        return pickle.load(in_handle)


def build_paths(paths):

    if isinstance(paths, str):
        print(f"{paths} is a single string. Did you mean to use build_path?")

    for path in paths:

        if not os.path.exists(path):
            build_path(path)
            print(f"Created directory: {path}")


def build_path(path):
    os.makedirs(path)
