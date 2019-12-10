import sqlalchemy as db
from exceptions import CreateEngineException, NotCompletedOutputException

class Analyzer:
    def __init__(self):
        self.planning_time = ''
        self.execution_time = ''
        self._sort_names = []

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

def parse_explain(value):
    an = Analyzer()
    check_start = lambda x, y: x.startswith(y)
    sort_names = lambda x: x.split(',')
    for v in value:
        data = v[0]
        if check_start(data, 'Planning'):
            an.planning_time = data.split(':')[1]
        if check_start(data, 'Execution'):
            an.execution_time = data.split(':')[1]
        if check_start(data, 'Sort Key'):
            an.sort_names = sort_names(data)
        print(data)