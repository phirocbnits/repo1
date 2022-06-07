from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql+pymysql://root:root@localhost/flask1', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(30)), 
   Column('lastname', String(30)),
)
meta.create_all(engine)