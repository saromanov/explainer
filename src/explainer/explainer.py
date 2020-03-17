from exceptions import CreateEngineException, NotCompletedOutputException, NoTasksException
from task import Task
from db import create_engine, connect
from metrics import Metrics, MetricsStore, from_csv
from plot import show
from dump import Dump
from load import load

class Explainer:
    def __init__(self, connect_path, *args, **kwargs):
        self._session = connect(create_engine(connect_path))
        self._metric_names = kwargs.get('metric_names', ['planning_time'])
        self._method_names = kwargs.get('method_names', ['mean', 'median'])
        self._tasks = []
        self._loaded_tasks = []
        self._metrics_store = {}
    
    def add_task(self, parent_title, title, query, *args, **kwargs):
        ''' adding new task(query)
        '''
        self._tasks.append(Task(parent_title, title, query, *args, **kwargs))
    
    def from_file(self, path):
        ''' Getting queries from the file
        At the each line should be new query
        '''
        with open(path) as f:
            data = f.readlines()
        for x in data:
            self._tasks.append(Task(x))
    
    def load_task(self, path):
        '''
        loading of saved tasks. These tasks
        can be loaded for compare with other tasks
        '''
        df = from_csv(path)
    
    def save(self, path:str):
        '''
        save provides saving of the data metrics
        '''
        if not self._metrics:
            raise NoMetricsException('Metrics is not loaded')
        if len(self._tasks) == 0:
            raise NoTasksException('Tasks is not defined')
        for t in self._tasks:
            metrics = self._metrics_store[t.title()]
            d = Dump(t, metrics)
            d.save(path)
    
    def load(self, path:str):
        '''
        loading of the dumped data
        '''
        if not path:
            raise Exception('path is not defined')
        load(path)

    def apply(self, *args, **kwargs):
        ''' applying of tasks
            optional:
                show_plot - showing of the plot via matplotlib
                tasks - getting plot for list of tasks
        '''
        if len(self._tasks) == 0:
            raise NoTasksException('Tasks is not defined')
        print('Loaded tasks: ')
        default_tasks = []
        for t in self._tasks:
            print(t.title())
            default_tasks.append(t.title())
        m = Metrics([t.run(self._session) for t in self._tasks])
        self._metrics = m
        tasks = kwargs.get('tasks') if 'tasks' in kwargs else default_tasks
        for task in tasks:
            data = m[task]
            self._metrics_store[task] = MetricsStore(task, \
                self._metric_names, \
                self._method_names, \
                m,
                task
                )
            if kwargs.get('show_plot'):
                show(data['planning_time'], data['execution_time'])