from bs4 import BeautifulSoup


def bs4_crawling(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select(
        'div.newcx-container > div.newcx-body > div.newcx-main > div.newcx-list > ul.baby-product-list > li')

    count = 0
    for element in search_result:
        count += 1
        print(count)
        e = element.select_one('a.baby-product-link > dl.baby-product-wrap')
        img = "https://" + e.select_one(' dt.image > img')['src']
        name = e.select_one('dd > div.name').text
        title = e.select_one('dd > div > div > div > em > strong').text
        # print("제조사: " + re.split(' |,', name.lstrip())[0])


