from typing import List
from parse import parse_explain
from db import explain, rows_count
from parse import Analyzer

class Task:
    ''' defines query as a task
    '''
    def __init__(self, parent_title, title, query, *args, **kwargs):
        self.query = query
        self.rows_count = kwargs.get('rows_count', 0)
        self.table = kwargs.get('table')
        self._parent_title = parent_title
        self._title = title
        self._times = kwargs.get('times', 10)
    
    def title(self) -> str:
        return self._title
    
    def parent_title(self) -> str:
        return self._parent_title
    
    def to_json(self):
        '''
        converting of the Task object into
        JSON representation
        '''
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def __str__(self) -> str:
        return 'Title: {0}\nQuery: {1}\n Times:{2}'.format(self._title, self.query, self._times)
    
    def run(self, session) -> List[Analyzer]:
        if self.table:
            self._rows_count = rows_count(session, self.table)
        return [parse_explain(self._title, explain(session, self.query)) for x in range(self._times)]
    
    
    

    