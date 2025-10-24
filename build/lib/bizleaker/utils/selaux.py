import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options


def wait_for_find(driver, filter, criteria=By.XPATH, seconds=15, click=False, condition=EC.element_to_be_clickable, error=True):
    try:
        WebDriverWait(driver, seconds).until(
            condition((criteria, filter))
        )
        elem = driver.find_element(criteria, filter)
        if click:
            elem.click()
        return elem
    except:
        if error:
            raise
        else:
            return False


def wait_for_url(driver, url, accept=True, seconds=15, click=False, error=True):
    try:
        if accept:
            WebDriverWait(driver, seconds).until(
                lambda driver: driver.current_url == url
            )
        else:
            WebDriverWait(driver, seconds).until(
                lambda driver: driver.current_url != url
            )
        return driver.current_url
    except:
        if error:
            raise
        else:
            return False

def chrome(headless=True):
    options = chrome_Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(options=options)
    return driver


def firefox(headless=True):
    options = firefox_Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Firefox(options=options)
    return driver
