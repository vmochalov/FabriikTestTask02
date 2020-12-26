from selenium import webdriver

from settings import WEBDRIVER_FF_PATH, WEBDRIVER_CHROME_PATH


def setup_driver(driver_type="chrome"):
    if driver_type == "firefox":
        driver = webdriver.Firefox(WEBDRIVER_FF_PATH)
    else:
        driver = webdriver.Chrome(WEBDRIVER_CHROME_PATH)
    driver.maximize_window()
    return driver


def teardown_driver(driver):
    driver.delete_all_cookies()
    driver.close()
