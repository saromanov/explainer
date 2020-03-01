from parse import parse_explain
from db import explain

class Task:
    ''' defines query as a task
    '''
    def __init__(self, title, query, times=10):
        self._query = query
        self._title = title
        self._rows = 0
        self._times = times
    
    def title(self):
        return self._title

    def __str__(self):
        return 'Title: {0}\nQuery: {1}\n Times:{2}'.format(self._title, self._query, self._times)
    
    def run(self, session):
        return [parse_explain(self._title, explain(session, self._query)) for x in range(self._times)]
    
    
    

    