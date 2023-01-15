from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com')
driver.fullscreen_window()

size = driver.get_window_size()
width = size.get("width")
height = size.get("height")

print(f"{width}x{height}")