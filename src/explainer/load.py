import os
import pickle

def load(path:str):
    '''
    loading of the dumped data
    '''
    metrics = []
    for _, _, files in os.walk(path):
        for f in files:
            res_path = os.path.join(path, f)
            with open(res_path, 'rb') as f:
                metrics.append(pickle.load(f))
    print(metrics)