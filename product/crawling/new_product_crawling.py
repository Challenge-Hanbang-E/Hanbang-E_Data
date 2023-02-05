import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config.logger_config import logger
from product.crawling.bs4_crawling import bs4_crawling
from product.crawling.setting.coupang_driver_setting import driver_connection

def crawl_new():
    driver = driver_connection()

    # 카테고리 순서 main > sub > detail > taget


    first_subCategory = 1
    last_subCategory = 15

    first_detailCategory = 1
    last_detailCategory = 17


    for i in range(first_subCategory, last_subCategory + 1):

        for j in range(first_detailCategory, last_detailCategory + 1):

            try:
                mainCategory = driver.find_element(By.XPATH, '//*[@id="header"]/div/a')
                subCategory = driver.find_element(By.XPATH, f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/a')
                logger.info(f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/a')

                actions = ActionChains(driver)
                actions.move_to_element(mainCategory)
                actions.move_to_element(subCategory)
                actions.click(driver.find_element(By.XPATH, f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/div/div/ul/li[{j}]/a'))
                actions.perform()
                driver.implicitly_wait(10)

            except:
                logger.info(f"categroy log = {i}, {j}이상 부턴 없는 카테고리")
                break

            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, '//*[@id="searchSortingOrder"]/ul/li[5]/label'))
                time.sleep(2)
                actions.click(driver.find_element(By.XPATH, '//*[@id="searchSortingOrder"]/ul/li[5]/label'))
                actions.perform()
                time.sleep(2)

            except:
                logger.info(f"categroy log = {i}, {j} 실패")
                break

            print("crawl category", i, j)
            bs4_crawling(driver, i, j, 0, 0)

