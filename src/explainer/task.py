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
    
    def run(self, session):
        return [parse_explain(self._title, explain(session, self._query)) for x in range(self._times)]
    
    
    

    