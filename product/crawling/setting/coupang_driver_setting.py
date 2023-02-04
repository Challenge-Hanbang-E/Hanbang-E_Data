from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def driver_connection():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # 화면 사용 X
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.20 Safari/537.36")
    # options.add_argument("window-size=1900x1200")
    options.add_argument("--incognito")  # 시크릿 모드(쿠키 X)
    options.add_argument("--disable-popup-blocking")  # 광고 팝업 노출 X
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    # 크롤링 방지 설정 → undefined로 변경
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
                """
    })

    url = "https://www.coupang.com"
    driver.implicitly_wait(40)
    driver.get(url)

    return driver
