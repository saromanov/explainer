
engine = create_engine("postgresql://explainer:explainer@localhost/explainer")
session = connect(engine)
#parse_explain(explain(session, "SELECT * FROM explainer WHERE priority = 1;"))
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