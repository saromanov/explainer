
import sqlalchemy as db
from random import randrange
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

engine = create_engine("postgresql://explainer:explainer@localhost/explainer")
session = connect(engine))
metadata = db.MetaData()
emp = db.Table('explainer', metadata, 
    db.Column('id', db.Integer()),
    db.Column('priority', db.Integer()),
    db.Column('name', db.String(255)),)
query = db.insert(emp)
values_list = []
for i in range(2000000):
    values_list.append({'id': i, 'name': randomString(10), 'priority': randrange(1,10,1)})
ResultProxy = session.execute(query,values_list)
print(ResultProxy)