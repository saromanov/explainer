import os
import pickle
import pandas as pd
from metrics import Metrics
from task import Task

class Dump:
    def __init__(self, task:Task, metrics: MetricStore):
        self._metrics = metrics
        self._task = task
    
    def save(self, path:str):
        '''
        saving of the dump file
        '''
        if not path:
            raise Exception('path to Dump tasks is not defined')
        dir_path = os.path.join(path, self._task.parent_title())
        if not os.path.exists(dir_path):
            if not os.path.isdir(dir_path):
                self._mkdir(dir_path)
        result_path = self._get_dump_file_name(dir_path, self._task)
        tasks = self._task.to_json()
        metrics = self._metrics.to_json()
        print(tasks)
        print(metrics)
        data = {**tasks, **metrics}
        pickle.dump(data, open(result_path, 'wb'))
    
    def _mkdir(self, path:str):
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            if e.errno == errno.EEXIST:
                print('Directory {0} not created'.format(path))
            else:
                raise
    
    def _get_dump_file_name(self, path:str, task:Task):
        ''' return dump file name based on parent title
            and title from the task
        '''
        return os.path.join(path, task.title())

