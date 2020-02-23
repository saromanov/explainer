from parse import parse_explain
from db import explain

class Task:
    ''' defines query as a task
    '''
    def __init__(self, query, times=10):
        self._query = query
        self._rows = 0
        self._times = times
    
    def run(self, session):
        for x in range(self._times):
            parse_explain(explain(session, self._query))
    
    
    

    