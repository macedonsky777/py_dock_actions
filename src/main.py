from shop import Shop
#import sys
shop_manage = Shop(dbhost='db', dbuser='macdev1', dbpass='123321', dbname='Shops', dbport='3306')
shop_manage.test_shop()
#host = sys.argv[1]
#user = sys.argv[2]
#passwodr = sys.argv[3]
#
#shop = Shop(host, user, password)
#shop.create_shop()
#ids = shop.add_item("Pikachu", 777)
#print(ids)
#for id in ids:
#    res = shop.delete_item_by_id(id)
    
