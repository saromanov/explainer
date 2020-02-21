import sqlalchemy as db
from exceptions import CreateEngineException, NotCompletedOutputException
from task import Task


class Explainer:
    def __init__(self):
        self._tasks = []
    
    def add_task(self, query):
        self._tasks.append(Task(query))
    
    def from_file(self, path):
        ''' Getting queries from the file
        At the each line should be new query
        '''
        with open(path) as f:
            data = f.readlines()
        for x in data:
            self._tasks.append(Task(x)) 

def create_engine(path):
    if path is None:
        raise CreateEngineException('path for engine is empty')
    return db.create_engine(path)

def connect(engine):
    if engine is None:
        raise Exception('Engine is not defined')
    return engine.connect()

def explain(session, query):
    return session.execute('EXPLAIN ANALYZE {0}'.format(query)).fetchall()