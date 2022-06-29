import time
import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
#import mysql.connector


#db details
server = 'localhost' 
database = 'mysql' 
username = 'root' 
password = 'root'

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root",pw="root",db="dfsql"))

"""db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="fdsql")
mycursor = db.cursor()"""

def readNinsert(data_set):
    a = pd.read_csv(data_set,encoding='latin1')
    # Insert whole DataFrame into MySQL
    a.to_sql('store', con = engine, if_exists = 'append', chunksize = 1000)

def readNinsert1(data_set):
    a = pd.read_csv(data_set,encoding='latin1')
    # Insert whole DataFrame into MySQL
    a.to_sql('store1', con = engine, if_exists = 'append')
t1 = time.time()
data_list = ["ss1.csv","ss2.csv","ss3.csv"]
for data_set in data_list:
    readNinsert(data_set)
print("for works in: ", time.time()-t1)
t1 = time.time()
P=Pool()
P.map(readNinsert1, data_list)
P.close()
P.join()
print("for works in: ", time.time()-t1)