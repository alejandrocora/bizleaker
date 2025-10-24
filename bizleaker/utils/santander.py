from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bizleaker.utils.selaux import *
from bizleaker.utils.constants import *


class Santander():

    def __init__(self, driver, login_id):
        self.driver = driver
        self.login_id = login_id
        self.login_url = LOGIN_URL

    def login(self, login_password):
        self.driver.get(self.login_url)
        #wait_for_find(self.driver, 'onetrust-accept-btn-handler', criteria=By.ID, click=True) # For now, it doesn't seem to interrupt anything, but will stay here in case it does in the future
        wait_for_find(self.driver, 'inputDocuNumber', criteria=By.ID, condition=EC.presence_of_all_elements_located).send_keys(self.login_id)
        elem = wait_for_find(self.driver, 'pass-positions', criteria=By.CLASS_NAME, condition=EC.presence_of_all_elements_located)
        elem.send_keys(login_password)
        elem.send_keys(Keys.ENTER)

    def open_service(self):
        wait_for_url(self.driver, HOME_URL)
        self.driver.get('https://particulares.bancosantander.es/oneweb/transferencias')
        wait_for_find(self.driver, '//*[@id="Bizum en-GB"]', click=True)
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait_for_find(self.driver, '/html/body/section/div[4]/floating-menu/button', click=True)
        sleep(0.5)
        wait_for_find(self.driver, '/html/body/section/div[4]/floating-menu/div/div[2]', click=True)

    def service_send(self, number):
        if len(str(number)) < 9:
            print('[!] Invalid phone number.')
            return False
        elem = wait_for_find(self.driver, '/html/body/section/div[2]/div[3]/div[2]/div/div/input', condition=EC.presence_of_element_located)
        elem.clear()
        elem.send_keys(number)
        elem = self.driver.find_element(By.XPATH, '/html/body/section/div[2]/div[3]/div[2]/div/div/button').click()
        elem = self.driver.find_element(By.NAME, 'amount').clear()
        elem = self.driver.find_element(By.NAME, 'amount').send_keys('0.5')
        elem = self.driver.find_element(By.XPATH, '//button[@ng-click="setFormData()"]').click()
        return True

    def service_get_name(self):
        if wait_for_find(self.driver, '//*[@id="user-no-register"]', seconds=2, error=False):
            wait_for_find(self.driver, '/html/body/div[4]/div/div[2]/button[1]', click=True)
            self.driver.execute_script("window.history.go(-1)")
            return False
        try:
            wait_for_url(self.driver, SERVICE_NAME, accept=False)
            elem = wait_for_find(self.driver, 'contact_alias_ord', criteria=By.CLASS_NAME, condition=EC.presence_of_element_located)
            return elem.text
        except Exception as e:
            self.driver.get(MOVEMENTS_URL)
            raise e

    def service_go_back(self):
        self.driver.execute_script("window.history.go(-1)")
        sleep(2)
        try:
            wait_for_find(self.driver, 'contact__remove', criteria=By.CLASS_NAME, click=True)
        except Exception as e:
            print(e)