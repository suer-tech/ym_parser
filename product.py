import psycopg2
from db_conf import conn, cur


class Product:
    def __init__(self, data):
        try:
            self.product_id = data['productId']
            self.title = data['modelAwareTitles']['raw']
            self.characteristics = [item for item in data['skuAwareSpecs']['friendly']]
            self.price = data['prices']['value']
            if 'discount' in data['prices']:
                self.old_price = data['prices']['discount']['oldMin']
                self.discount = data['prices']['discount']['absolute']
            else:
                self.old_price = None
                self.discount = None
        except KeyError as e:
            print("Ошибка при получении данных:", e)

    def save_to_database(self, conn):
        try:
            cur = conn.cursor()
            sql = "INSERT INTO products (product_id, title, characteristics, price, old_price, discount) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (self.product_id, self.title, self.characteristics, self.price, self.old_price, self.discount))
            conn.commit()
            print("Данные успешно сохранены в базе данных")
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Ошибка при сохранении данных:", e)
            print("Данные с product_id={} уже существуют в базе данных".format(self.product_id))
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print("Ошибка при сохранении данных:", error)


def close_connection():
    cur.close()
    conn.close()