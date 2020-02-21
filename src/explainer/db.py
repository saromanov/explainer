import sqlalchemy as db

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