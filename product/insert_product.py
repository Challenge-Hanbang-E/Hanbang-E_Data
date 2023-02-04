import json

from config.db_connect import cur, conn
from config.logger_config import logger

i = 1
j = 1

while i <= 15:
    try:
        product_file_path = f'./products_data/product_{i}_{j}.json'
        with open(product_file_path, "r") as product_file:
            values_data = json.load(product_file)
            products = values_data['product']
            logger.info(f"product_{i}_{j}.json: {len(products)}")
            values = str(products).replace("[", "").replace("]", "").replace('"', "")
            sql = "INSERT INTO product (NAME, PRICE, IMG, STOCK, SALES, ON_SALE) VALUES" + values
            cur.execute(sql)
            conn.commit()

            j += 1
    except:
        logger.info(f"product_{i}_{j}.json 존재 안함")
        j += 1
        if j > 17:
            i += 1
            j = 1

conn.close()
