from exceptions import CreateEngineException, NotCompletedOutputException
from task import Task
from db import create_engine, connect


class Explainer:
    def __init__(self, connect_path):
        self._session = connect(create_engine(connect_path))
        self._tasks = []
    
    def add_task(self, query):
        ''' adding new task(query)
        '''
        self._tasks.append(Task(query))
    
    def from_file(self, path):
        ''' Getting queries from the file
        At the each line should be new query
        '''
        with open(path) as f:
            data = f.readlines()
        for x in data:
            self._tasks.append(Task(x)) 
    
    def apply(self):
        ''' applying of tasks
        '''
        if len(self._tasks) == 0:
            raise Exception('Tasks is not defined')