# sqlalchemy select statement tutorial
import sqlalchemy as sql

db = sql.create_engine('sqlite:///tutorial.db')

db.echo = True

metadata = sql.MetaData(db)

users = sql.Table('users', metadata, autoload=True)

def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print row

s = users.select(users.c.name == 'kyle')
run(s)
s = users.select(users.c.age < 40)
run(s)

s = users.select(sql.and_(users.c.age < 40, users.c.name != 'Mary'))
run(s)
s = users.select(sql.or_(users.c.age < 40, users.c.name != 'Mary'))
run(s)
s = users.select(not_(users.c.name == 'kyle'))
run(s)

s = users.select(users.c.name.startswith('k'))
run(s)
s = users.select(users.c.name.like('%a'))
run(s)
s = users.select(users.c.name.endswith('e'))
run(s)

s = users.select(users.c.age.between(20,30))
run(s)
s = users.select(users.c.name.in_('kyle','joe'))
run(s)

# for sql functions use "func"
s = users.select(sql.func.substr(users.c.name,2,1) == 'a')
run(s)

s = sql.select([users],users.c.name != 'carl')
run(s)

s = sql.select([sql.func.count(users.c.user_id)])
run(s)
s = sql.select([sql.func.count('*')],from_obj=[users])
run(s)

