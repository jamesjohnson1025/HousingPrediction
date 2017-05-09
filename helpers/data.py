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
'''
def split_train_test(data,test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]
'''

def test_set_check(identifier,test_ratio,hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio


def split_train_test_by_id(data,test_ratio,id_column,hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_,test_ratio,hash))
    return data.loc[~in_test_set],data.loc[in_test_set]






