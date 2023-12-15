import unittest
from shop import Shop


class TestMysql(unittest.TestCase):
    def __init__(self, dbhost, dbuser, dbpass, dbname, dbport):
        self._mydb = self.mydb
        self._mycursor = self._mydb.cursor()
        print("Nice!")
    
    def test_shop(self):
        self.test_connection()

if __name__ == "__main__":
    print("Wait, testing...")
    unittest.main()
