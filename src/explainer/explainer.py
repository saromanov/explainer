import sqlalchemy as db
from exceptions import CreateEngineException, NotCompletedOutputException

class Analyzer:
    def __init__(self):
        self.planning_time = ''
        self.execution_time = ''

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
    check_ms = lambda x, y: x.startswith(y)
    for v in value:
        data = v[0]
        if check_ms(data, 'Planning'):
            an.planning_time = data.split(':')[1]
        if check_ms(data, 'Execution'):
            an.execution_time = data.split(':')[1]