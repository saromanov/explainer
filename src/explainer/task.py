from typing import List
from parse import parse_explain
from db import explain, rows_count
from parse import Analyzer

class Task:
    ''' defines query as a task
    '''
    def __init__(self, title, query, *args, **kwargs):
        self._query = query
        self._title = title
        self._rows_count = kwargs.get('rows_count')
        self._times = kwargs.get('times', 10)
        self._table = kwargs.get('table')
    
    def title(self) -> str:
        return self._title
    
    def rows_count(self):
        return self._rows_count

    def __str__(self) -> str:
        return 'Title: {0}\nQuery: {1}\n Times:{2}'.format(self._title, self._query, self._times)
    
    def run(self, session) -> List[Analyzer]:
        if self._table:
            self._rows_count = rows_count(session, self._table)
        return [parse_explain(self._title, explain(session, self._query)) for x in range(self._times)]
    
    
    

    