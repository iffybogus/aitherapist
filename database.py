#import sqlalchemy
#print(sqlalchemy.__version__)
#import pymysql
import os
from sqlalchemy import create_engine, text

def load_clients():
  with engine.connect() as conn:
    result = conn.execute(text("select * from clients"))
    return result.all()
    
db_connection = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection, 
  connect_args = {
    "ssl": {
       "ssl_ca":"/etc/ssl/cert.pem"
    }
  })

print(load_clients())

