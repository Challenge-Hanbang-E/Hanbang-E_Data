import json

from db_connect import cur, conn
from logger_config import logger

i = 1
j = 1
last_j = 3

while j <= last_j:
    product_file_path = f'./products/product_{i}_{j}.json'
    with open(product_file_path, "r") as product_file:
        values_data = json.load(product_file)
        products = values_data['product']
        logger.info(f"product_{i}_{j}.json: {len(products)}")
        values = str(products).replace("[", "").replace("]", "").replace('"', "")
        sql = "INSERT INTO product (NAME, PRICE, IMG, STOCK, SALES, ON_SALE) VALUES" + values
        cur.execute(sql)
        conn.commit()

        j += 1

conn.close()
