import os
import pickle

def load(path:str):
    '''
    loading of the dumped data
    '''
    if not os.path.exists(path):
        raise Exception(f'{path} is not exists')
    return [_pickle_load(f, path) for _,_, files in os.walk(path) for f in files]

def _pickle_load(f, path):
    res_path = os.path.join(path, f)
    with open(res_path, 'rb') as fl:
        return pickle.load(fl)