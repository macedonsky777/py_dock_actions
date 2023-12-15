import unittest
import coverage  # Add this import

# Start code coverage measurement
cov = coverage.Coverage()
cov.start()

from shop import Shop

class TestShop(unittest.TestCase):
    def setUp(self):
        # Setup code that should be run before each test method
        self.shop_manage = Shop(dbhost='localhost', dbuser='root', dbpass='qwerty1234', dbname='Shops', dbport='3306')

    def test_shop_connection(self):
        self.shop_manage.test_shop()
        # Add assertions based on the expected behavior of your test

if __name__ == "__main__":
    print("Wait, testing...")

    # Discover and run the tests
    unittest.main()

    # Stop code coverage measurement and generate the report
    cov.stop()
    cov.save()

    # Optionally, print the coverage report
    cov.report()
