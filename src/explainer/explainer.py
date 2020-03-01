from exceptions import CreateEngineException, NotCompletedOutputException
from task import Task
from db import create_engine, connect
from metrics import Metrics, from_csv
from plot import show

class Explainer:
    def __init__(self, connect_path):
        self._session = connect(create_engine(connect_path))
        self._tasks = []
    
    def add_task(self, title, query, *args, **kwargs):
        ''' adding new task(query)
        '''
        self._tasks.append(Task(title, query, *args, **kwargs))
    
    def from_file(self, path):
        ''' Getting queries from the file
        At the each line should be new query
        '''
        with open(path) as f:
            data = f.readlines()
        for x in data:
            self._tasks.append(Task(x))
    
    def read_metrics(self, path):
        '''
        reading metrics from the file
        '''
        df = from_csv(path)
    
    def save(self, path):
        '''
        save provides saving of the data metrics
        '''
        if not self._metrics:
            raise NoMetricsException('Metrics is not loaded')


    
    def apply(self, *args, **kwargs):
        ''' applying of tasks
        '''
        if len(self._tasks) == 0:
            raise NoTasksException('Tasks is not defined')
        print('Loaded tasks: ')
        for t in self._tasks:
            print(t.title())
        m = Metrics([t.run(self._session) for t in self._tasks])
        self._metrics = m
        print(m.median('planning_time',task='priority10'), m.std('planning_time'))
        tasks = kwargs.get('tasks') if 'tasks' in kwargs else []
        for task in tasks:
            data = m[task]
            if kwargs.get('show_plot'):
                show(data['planning_time'], data['execution_time'])