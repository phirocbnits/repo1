import mysql.connector

my_db=mysql.connector.connect(user='root',password='root', host='localhost')
my_cur=my_db.cursor()
my_cur.execute("CREATE DATABASE flask1")