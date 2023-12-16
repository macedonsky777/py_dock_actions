import unittest
from shop import Shop


class TestMysql(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("mysql", "root", "qwerty1234", "shop", 3306 )
        self.shop.create_main_db("shop")
        print("Nice!")
    
    def test_create_item(self):
        self.shop.create_shop()
        res = self.shop.add_item("test pet1", 20)
        print(f"RES: {res}")
        self.assertTrue(len(res) > 0)
    
    def tearDown(self):
        self.shop.delete_shop()


if __name__ == "__main__":
    print("Wait, testing...")
    unittest.main()
