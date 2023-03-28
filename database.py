#import sqlalchemy
#print(sqlalchemy.__version__)
#import pymysql
from sqlalchemy import create_engine, text

def load_clients():
  with engine.connect() as conn:
    result = conn.execute(text("select * from clients"))
    return result.all()
    
db_connection = "mysql+pymysql://3p5hvajgf7l768p9b6ya:pscale_pw_odbVEmFRLrPRd2dlLX7mfbDZKJH1N2K9p72SESoFnOk@us-east.connect.psdb.cloud/aitherapist?charset=utf8mb4"

engine = create_engine(db_connection, 
  connect_args = {
    "ssl": {
       "ssl_ca":"/etc/ssl/cert.pem"
    }
  })

print(load_clients())

