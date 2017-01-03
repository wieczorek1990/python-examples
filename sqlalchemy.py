from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://cesar:cesar@localhost:5432/cesar', echo=True)
Base = declarative_base(bind=engine)
session = scoped_session(sessionmaker(engine))
connection = session.connection()

result = connection.execute("select 'hello world'")
for row in result:
    print row[0]

