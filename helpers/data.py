"""
    Fetch data from https://github.com/ageron/handson-ml/raw/master/datasets

    extract to data folder


    Author : James K J (kj.james2010@vitalum.ac.in)

"""


import os
import tarfile
import pandas as pd
import numpy as np
import hashlib
from six.moves import urllib


DATASETS_URL = 'https://github.com/ageron/handson-ml/raw/master/datasets'
HOUSING_PATH = '/home/jamesjohnson92/Workspace/Assignments/Housing Prices/src/data'
HOUSING_URL  = DATASETS_URL + '/housing/housing.tgz'


def fetch_housing_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):

    if not os.path.exists(housing_path):
        os.makedirs(housing_path)

    tgz_path = os.path.join(housing_path,'housing.tgz')
    urllib.request.urlretrieve(housing_url,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path,'housing.csv')
    return pd.read_csv(csv_path)






