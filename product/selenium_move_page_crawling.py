from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from coupang_driver_setting import driver_connection
from bs4_crawling import bs4_crawling
from logger_config import logger

driver = driver_connection()

# 카테고리 순서 main > sub > detail > taget

def next_page(i, j, k):
    for page_button_num in range(first_page_button, last_page_button + 1):
        if page_button_num == 12:
            button_num = page_button_num
        elif page_button_num == 13:
            continue
        else:
            button_num = page_button_num % 12
        if button_num != 2:
            page_num = f'//*[@id="product-list-paging"]/div/a[{button_num}]'
            try:
                page = driver.find_element(By.XPATH, page_num)
                driver.execute_script("arguments[0].click();", page)
                driver.implicitly_wait(40)
            except:
                break

        bs4_crawling(driver, i, j, k, page_button_num)


first_subCategory = 1
last_subCategory = 15

first_detailCategory = 1
last_detailCategory = 17

first_targetCategory = 1
last_targetCategory = 14

first_page_button = 2
last_page_button = 20


for i in range(first_subCategory, last_subCategory + 1):
    lastDetailCategory = False

    for j in range(first_detailCategory, last_detailCategory + 1):
        if lastDetailCategory:
            break

        for k in range(first_targetCategory, last_targetCategory + 1):
            logger.info(f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/a')
            mainCategory = driver.find_element(By.XPATH, '//*[@id="header"]/div/a')
            subCategory = driver.find_element(By.XPATH, f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/a')

            try:
                detailCategory = driver.find_element(By.XPATH,
                                                     f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/div/div/ul/li[{j}]/a')
            except:
                lastDetailCategory = True
                break

            actions = ActionChains(driver)
            actions.move_to_element(mainCategory)
            actions.move_to_element(subCategory)
            actions.move_to_element(detailCategory)

            try:
                targetCategory = f'//*[@id="gnbAnalytics"]/ul[1]/li[{i}]/div/div/ul/li[{j}]/div/ul/li[{k}]/a'
                logger.info(f"category log = {i}, {j}, {k}")
                actions.click(driver.find_element(By.XPATH, targetCategory))
                actions.perform()
                driver.implicitly_wait(40)

            except:
                logger.info(f"categroy log = {i}, {j}, {k} 실패")
                break

            next_page(i, j, k)
