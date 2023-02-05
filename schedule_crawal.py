import schedule
import time
import datetime

from product.crawling.new_product_crawling import crawl_new
from product.insert_product import insert_data


def job():
    print(datetime.datetime.now())
    print("new Crawl")
    crawl_new()
    print("insert new data")
    insert_data()
    print("insert complete")


schedule.every().day.at("18:00:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

