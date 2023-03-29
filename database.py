#import sqlalchemy
#print(sqlalchemy.__version__)
#import pymysql
import os
from sqlalchemy import create_engine, text

def load_client_from_db(id):
  with engine.connect() as conn:
    values = {'val': id}
    result = conn.execute(
      text('SELECT * FROM clients WHERE id = :val'), 
      values
    )
    rows =  result.all()
      
    if len(rows) == 0:
      return None
    else:
      print("type", type(rows[0]))
      return None

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

#print(load_clients())

