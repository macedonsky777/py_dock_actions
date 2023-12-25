from shop import Shop
import sys
#shop_manage = Shop(dbhost='localhost', dbuser='root', dbpass='qwerty123', dbname='Shops', dbport='3306')
#shop_manage.test_shop()
host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
#
shop = Shop(host="mysql", user="root", password="qwerty1234", dbname="popl", dbport=3306)
shop.create_shop()
ids = shop.add_item("Pikachu", 777)
print(ids)
for id in ids:
    res = shop.delete_item_by_id(id)
    
