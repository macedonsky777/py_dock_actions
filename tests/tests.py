import unittest
import sys
import os

# Add the path to the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shop import Shop

class TestShop(unittest.TestCase):
    def setUp(self):
        # Setup code that should be run before each test method
        self.shop_manage = Shop(dbhost='mysql', dbuser='root', dbpass='qwerty1234', dbname='Shops', dbport='3306')

    def test_shop_connection(self):
        self.shop_manage.test_shop()
        # Add assertions based on the expected behavior of your test

if __name__ == "__main__":
    print("Wait, testing...")
    unittest.main()
