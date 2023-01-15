import json
import random
from bs4 import BeautifulSoup

from logger_config import logger


def bs4_crawling(driver, i, j, k, page):
    file_path = f'./products/product_{i}_{j}.json'
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    except:
        data = {"product": []}

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select(
        'div.newcx-container > div.newcx-body > div.newcx-main > div.newcx-list > ul.baby-product-list > li')

    if page < 12:
        page = page - 1
    else:
        page = page - 3

    count = 0
    with open(file_path, 'w') as outfile:
        for element in search_result:
            count += 1
            sales = random.randrange(1, 10000)
            try:
                e = element.select_one('a.baby-product-link > dl.baby-product-wrap')
                img = "https://" + e.select_one(' dt.image > img')['src']
                product_name = e.select_one('dd > div.name').text.strip().replace('"', "").replace("'", "")
                price = e.select_one('dd > div > div > div > em > strong').text.replace(",", "")

                json_values = f"('{product_name}', {price}, '{img}', {1000000}, {sales}, {True})"
                data['product'].append(json_values)

            except:
                logger.info(f"실패: 카테고리: {i} > {j} > {k}, 페이지: {page}, 카운트: {count}")


        json.dump(data, outfile, indent=1, ensure_ascii=False)




