import json
from datetime import datetime

from config.db_connect import cur, conn
from config.logger_config import logger

def insert_data():
    today = datetime.today().strftime("%Y-%m-%d")

    try:
        product_file_path = f'product/new_products_data/{today}.json'
        with open(product_file_path, "r") as product_file:
            values_data = json.load(product_file)
            products = values_data['product']
            values = str(products).replace("[", "").replace("]", "").replace('"', "")
            sql = "INSERT INTO product (NAME, PRICE, IMG, STOCK, SALES, ON_SALE) VALUES" + values
            cur.execute(sql)
            conn.commit()

    except:
        logger.info(f"{today}.json 존재 안함")

    conn.close()
