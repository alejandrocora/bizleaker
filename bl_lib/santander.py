from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Santander():
    def __init__(self, driver, login_id):
        self.driver = driver
        self.login_id = login_id
        self.login_url = 'https://particulares.bancosantander.es/login/'

    def login(self, login_password):
        self.driver.get(self.login_url)
        sleep(1)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))
        )
        elem = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        elem.click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'inputDocuNumber'))
        )
        elem = self.driver.find_element(By.ID, 'inputDocuNumber')
        elem.send_keys(self.login_id)
        elem = self.driver.find_element(By.CLASS_NAME, 'pass-positions')
        elem.send_keys(login_password)
        elem.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.current_url != "https://particulares.bancosantander.es/login/"
        )

    def open_bizum(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()=" Bizum "]'))
        )
        elem = self.driver.find_element(By.XPATH, '//span[text()=" Bizum "]')
        elem.click()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def bizum_send(self, number):
        WebDriverWait(self.driver, 15).until(
            lambda driver: self.driver.current_url == "https://pagosinmediatos.bancosantander.es/PAINOP_BIZUMWEB/index.jsp#!/movimientos"
        )
        self.driver.get('https://pagosinmediatos.bancosantander.es/PAINOP_BIZUMWEB/index.jsp#!/enviar')
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'contactNumber'))
        )
        elem = self.driver.find_element(By.NAME, 'contactNumber')
        elem.send_keys(number)
        elem = self.driver.find_element(By.XPATH, '//button[@ng-click="addNewContact($event)"]')
        elem.click()
        elem = self.driver.find_element(By.NAME, 'amount')
        elem.send_keys('0.5')
        elem = self.driver.find_element(By.XPATH, '//button[@ng-click="setFormData()"]')
        elem.click()

    #def bizum_delete_number(self):
    #    elem = self.driver.find_element(By.XPATH, '//div[@class="contact__remove"]')
    #    elem.click()

    def bizum_get_name(self):
        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: self.driver.current_url != "https://pagosinmediatos.bancosantander.es/PAINOP_BIZUMWEB/index.jsp#!/enviar"
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'contact_alias_ord'))
            )
            elem = self.driver.find_element(By.CLASS_NAME, 'contact_alias_ord')
            return elem.text
        except Exception as e:
            self.driver.get('https://pagosinmediatos.bancosantander.es/PAINOP_BIZUMWEB/index.jsp#!/movimientos')
            raise e
