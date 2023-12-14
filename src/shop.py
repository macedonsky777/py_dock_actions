from db import Mysql
class Shop(Mysql):
    def __init__(self, dbhost, dbuser, dbpass, dbname, dbport):
        super().__init__(dbhost, dbuser, dbpass, dbname, dbport)
        self._mydb = self.mydb
        self._mycursor = self._mydb.cursor()

    def create_main_db(self, db_name):
        self.create_db(dbname=db_name)

    def create_shop(self, shop_name):
        self.create_table(tablename=shop_name)
        print(f"Creating a shop with table named {shop_name}")

    def add_item(self, shop_name, item_name, item_price):
        self.insert_in_table(tablename=shop_name, val=(item_name, item_price))
        print(f"Adding item to {shop_name}: {item_name} priced at {item_price}")

    def delete_item(self, shop_name, del_item_name):
        self.delete_from_table(tablename=shop_name, delitemname=del_item_name) 
        print(f"Deleting {del_item_name} from {shop_name} was successfull.")

    def delete_shop(self, shop_name):
        self.drop_table(tablename=shop_name)
        print(f"Deleting {shop_name} was successfull.")

    def show_all_staff(self):
        databases = self.show_all()
        print(databases)

    def test_shop(self):
        self.test_connection()

#Usage
shop_manage = Shop(dbhost='db', dbuser='macdev1', dbpass='123321', dbname='Shops', dbport='3306')

shop_manage.test_shop()
#shop_manage.create_main_db("Shops")
#shop_manage.create_shop("Spooky_stuff")
#shop_manage.add_item("Spooky_stuff", "putin_mask", 1)
#shop_manage.show_all_staff("Spooky_stuff")
#shop_manage.delete_item("Spooky_stuff", "putin_mask")
#shop_manage.show_all_staff("Spooky_stuff")
#shop_manage.delete_shop("Spooky_stuff")
#shop_manage.show_all_staff()
