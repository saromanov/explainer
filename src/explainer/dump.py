import os
from metrics import Metrics
from tasks import Task 

class Dump:
    def __init__(self, task:Task, metrics: Metrics):
        self._metrics = metrics
        self._task = task
    
    def save(self, path:str):
        if not path:
            raise Exception('path to Dump tasks is not defined')
        mkdir(path)
    
    def mkdir(self, path:str):
        try:
            os.mkdir(path)
        except OSError as e:
            if e.errno == errno.EEXIST:
                print('Directory {0} not created'.format(path))
            else:
                raise
    
    def get_dump_file_name(self, task:Task):
        ''' return dump file name based on parent title
            and title from the task
        '''
        parent_title = task.parent_title()
        title = task.title()
        os.path.join(parent_title, title)

