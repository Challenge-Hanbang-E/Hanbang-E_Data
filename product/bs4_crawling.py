import json
from bs4 import BeautifulSoup

from db_connect import cur, conn

file_path = 'hanbange.json'

try:
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
except:
    data = {"product": []}

def bs4_crawling(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select(
        'div.newcx-container > div.newcx-body > div.newcx-main > div.newcx-list > ul.baby-product-list > li')

    count = 0
    with open(file_path, 'w') as outfile:
        for element in search_result:
            count += 1
            print(count)
            e = element.select_one('a.baby-product-link > dl.baby-product-wrap')
            img = "https://" + e.select_one(' dt.image > img')['src']
            title = e.select_one('dd > div.name').text.strip()
            price = e.select_one('dd > div > div > div > em > strong').text.replace(",", "")
            print(img)
            print(title)
            print(price)
            query = "INSERT INTO product(NAME, PRICE, IMG, STOCK, SALES, ON_SALE) VALUES (%s, %s, %s, 100, 0, True)"
            values = (title, int(price), img)
            cur.execute(query, values)
            conn.commit()

            data['product'].append({
                "name": title,
                "price": price,
                "img": img,
                "stock": 100,
                "sales": 0,
                "on_sale": True
            })

        json.dump(data, outfile, indent=2, ensure_ascii=False)



