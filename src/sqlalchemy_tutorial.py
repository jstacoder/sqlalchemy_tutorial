# sqlalchemy tutorial
import sqlalchemy as sqldb
from sqlalchemy import BoundMetaData

db = sqldb.create_engine('sqlite:///tutorial.db')
db.echo = False

metadata = BoundMetaData(db)

users = sqldb.Table('users', metadata,
    sqldb.Column('user_id',sqldb.Integer,primary_key=True),
    sqldb.Column('name', sqldb.String(55)),
    sqldb.Column('age',sqldb.Integer),
    sqldb.Column('password',sqldb.String),
)

users.create()

i = users.insert()
i.execute(name='Mary',age=30,password='secret')
i.execute({'name': 'kyle', 'age': 28},
          {'name': 'susan', 'age':30},
          {'name': 'carl', 'age':40})

s = users.select()
rs = s.execute()

row = rs.fetchone()
print 'Id:', row[0]
print 'Name:', row['name']
print 'Age:', row.age
print 'Password:', row[users.c.password]


for row in rs:
    print row.name, 'is', row.age, 'years old'

