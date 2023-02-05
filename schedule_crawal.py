import schedule
import time
import datetime

from product.crawling.new_product_crawling import crawl_new
from product.insert_product import insert_data
from slack_msg import send_slack_msg


def job():
    send_slack_msg('크롤링 시작', str(datetime.datetime.now()))
    print(datetime.datetime.now())
    print("new Crawl")
    crawl_new()
    send_slack_msg('크롤링 완료', str(datetime.datetime.now()))
    print("insert new data")
    send_slack_msg('데이터 삽입', str(datetime.datetime.now()))
    insert_data()
    print("insert complete")
    send_slack_msg('데이터 삽입 완료', str(datetime.datetime.now()))


schedule.every().day.at("09:00:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

