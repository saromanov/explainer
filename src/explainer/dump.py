import os
import pickle
from metrics import Metrics
from task import Task 

class Dump:
    def __init__(self, task:Task, metrics: Metrics):
        self._metrics = metrics
        self._task = task
    
    def save(self, path:str):
        if not path:
            raise Exception('path to Dump tasks is not defined')
        if not os.path.exists(path):
            if not os.path.isdir(path):
                self._mkdir(path)
        try:
            os.chmod(path, 0o777)
        except PermissionError:
            raise Exception('access denied to {0}'.format(path))
        result_path = os.path.join(path, self._get_dump_file_name(self._task))
        title = self._task.title()
        metrics = self._metrics[title]
        data = {k:v for m in metrics}
        pickle.dump(data, open(result_path, 'wb'))
    
    def _mkdir(self, path:str):
        try:
            os.mkdir(path)
        except OSError as e:
            if e.errno == errno.EEXIST:
                print('Directory {0} not created'.format(path))
            else:
                raise
    
    def _get_dump_file_name(self, task:Task):
        ''' return dump file name based on parent title
            and title from the task
        '''
        parent_title = task.parent_title()
        title = task.title()
        os.path.join(parent_title, title)

