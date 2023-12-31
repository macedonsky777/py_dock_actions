import mysql.connector
import pymysql
from pymysql import Error
from time import sleep

class Mysql():
    def __init__(self, dbhost, dbuser, dbpass, dbport):
        
        max_retries = 30
        retries = 0
        
        while True:
            try:
                self.mydb = mysql.connector.connect(
                    host=dbhost,
                    user=dbuser,
                    password=dbpass,
                    port=dbport
                )

                print("MySQL is ready.")
                break
            except mysql.connector.Error as err:
                
                print(f"Waiting for MySQL... ({err})")
                sleep(1)
                retries += 1

                if retries >= max_retries:
                    print("Unable to connect to MySQL. Exiting.")
                    exit(1)
                    
        self._mycursor = self.mydb.cursor()
                
    def create_db(self, dbname):
        self.dbname = dbname
        self._mycursor.execute("CREATE DATABASE IF NOT EXISTS " + dbname)

    def create_table(self, tablename):
        self.tablename = tablename
        self._mycursor.execute(f"CREATE TABLE {tablename} (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price INT NOT NULL)")

    def insert_in_table(self, tablename, item, price):
        sql = f"INSERT INTO {tablename} (item, price) VALUES ('{item}', {price})"
        return self.execute(sql)
        

    def delete_from_table(self, tablename, delitemname):
        self.tablename = tablename
        self.delitemname = delitemname
        sql_del = f"DELETE FROM {tablename} WHERE item = %s"
        self._mycursor.execute(sql_del, (delitemname,))

    def drop_table(self, tablename):
        drop_table_sql = f"DROP TABLE {tablename}"
        self.execute(drop_table_sql)

    def show_all(self):
        self._mycursor.execute("SHOW DATABASES")
        databases = self._mycursor.fetchall()
        return [db[0] for db in databases]

    def execute(self, text):
        try:
            if not self._mycursor:
                self._mycursor = self.mydb.cursor()

            self._mycursor.execute(text)
            results = self._mycursor.fetchall()
            self.mydb.commit()
            return results
        except Exception as e:
            print(f"Error executing query: {e}")
            self.mydb.rollback()
            return []



    def test_connection(self):
        try:
            self.mydb.ping(reconnect=True)
            print("Connected to the database!")
            self.mydb.close()
        except Error as e:
            print(f"An error occurred: {e}")
            self._mydb.close()
