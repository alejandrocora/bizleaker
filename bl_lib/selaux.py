import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options

def headless_chrome():
    options = chrome_Options()
    options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(options=options)
    return driver

def headless_firefox():
    options = firefox_Options()
    options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Firefox(options=options, service_log_path=os.devnull)
    return driver
