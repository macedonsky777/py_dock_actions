import mysql.connector
import pymysql
from pymysql import Error

class Mysql():
    def __init__(self, dbhost, dbuser, dbpass, dbname, dbport):
        self._dbhost = dbhost
        self._dbuser = dbuser
        self._dbpass = dbpass
        self._dbname = dbname
        self._dbport = dbport
        self.mydb = mysql.connector.connect(
            host = dbhost,
            user = dbuser,
            password = dbpass,
            port = dbport
                                            )
        self._mycursor = self.mydb.cursor()
        self._mycursor.execute(f"USE {dbname}")

    def create_db(self, dbname):
        self.dbname = dbname
        self._mycursor.execute("CREATE DATABASE " + dbname)

    def create_table(self, tablename):
        self.tablename = tablename
        self._mycursor.execute(f"CREATE TABLE {tablename} (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price INT NOT NULL)")

    def insert_in_table(self, tablename, val=("itemname", "itempricenum")):
        self.tablename = tablename
        self.val = val
        sql = f"INSERT INTO {tablename} (item, price) VALUES (%s, %s)"
        self._mycursor.execute(sql, val)

    def delete_from_table(self, tablename, delitemname):
        self.tablename = tablename
        self.delitemname = delitemname
        sql_del = f"DELETE FROM {tablename} WHERE item = %s"
        self._mycursor.execute(sql_del, (delitemname,))

    def drop_table(self, tablename):
        self.tablename = tablename
        drop_table_sql = f"DROP TABLE {tablename}"
        self._mycursor.execute(drop_table_sql)

        self._mycursor.execute(sql)

    def show_all(self):
        self._mycursor.execute("SHOW DATABASES")
        databases = self._mycursor.fetchall()
        return [db[0] for db in databases]

    def test_connection(self):
        try:
            self.mydb.ping(reconnect=True)
            print("Connected to the database!")
            self.mydb.close()
        except Error as e:
            print(f"An error occurred: {e}")
            self._mydb.close()
