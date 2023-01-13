import json

from db_connect import cur, conn

i = 9  # 고정 값
j = 1

products_data_combine = []

while j <= 5:  # j크기: 변동 값
    try:
        product_file_path = f'./product/product_{i}_{j}.json'

        with open(product_file_path, "r") as product_file:
            values_data = json.load(product_file)
            products = values_data['product']
            products_data_combine.append(products)
        j += 1

    except:
        print(f"member_{i}_{j}.json 존재 안함")
        j += 1


values = str(products_data_combine).replace("[", "").replace("]", "").replace('"', "")
sql = "INSERT INTO product (NAME, PRICE, IMG, STOCK, SALES, ON_SALE) VALUES" + values

cur.execute(sql)
conn.commit()
conn.close()
