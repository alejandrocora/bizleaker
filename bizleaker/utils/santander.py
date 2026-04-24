import sys

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from bizleaker.utils.constants import *


class Santander():

    def __init__(self, page, context, login_id, debug=False):
        self.page = page
        self.context = context
        self.login_id = login_id
        self.debug = debug

    def _pause(self, msg):
        if self.debug:
            input(f'[DEBUG] {msg} — press ENTER to continue...')

    def login(self, login_password):
        self.page.goto(LOGIN_URL, wait_until="domcontentloaded")
        try:
            self.page.locator('//*[@id="onetrust-accept-btn-handler"]').click(timeout=5000)
        except PlaywrightTimeoutError:
            pass
        self.page.locator('#inputDocuNumber').fill(self.login_id)
        self.page.locator('.pass-positions').first.click()
        self.page.keyboard.type(login_password)
        self.page.keyboard.press('Enter')

    def open_service(self):
        self.page.wait_for_url(HOME_URL)
        self._pause('at home page — about to go to transfers')
        self.page.goto('https://particulares.bancosantander.es/oneweb/transferencias', wait_until="domcontentloaded")
        self.page.wait_for_load_state('networkidle')
        self._pause('at transfers page — about to click Más opciones')
        self.page.click('a[id="Más opciones"]')
        self._pause('sidenav open — about to click Bizum')
        with self.context.expect_page() as new_page_info:
            self.page.click('a[id="Bizum"]')
        self.page = new_page_info.value
        self._pause('Bizum tab open — about to open floating menu')
        self.page.locator('.floating--button').wait_for()
        self.page.locator('.floating--button').click()
        self._pause('floating menu open — about to click send')
        self.page.locator('div.floating--item.send[ng-click="goEnviar()"]').wait_for()
        self.page.locator('div.floating--item.send[ng-click="goEnviar()"]').click()
        self._pause('send option clicked')

    def service_send(self, number):
        if len(str(number)) < 9:
            print('[!] Invalid phone number.', file=sys.stderr)
            return False
        self._pause(f'about to fill phone number {number}')
        self.page.locator('[name="contactNumber"]').wait_for()
        self.page.locator('[name="contactNumber"]').fill(str(number))
        self._pause('phone filled — about to confirm')
        self.page.locator('button[ng-click="addNewContact($event)"]').click()
        self._pause('phone confirmed — about to fill amount')
        self.page.locator('[name="amount"]').fill('0.5')
        self._pause('amount filled — about to submit')
        self.page.locator('button[ng-click="setFormData()"]').click()
        self._pause('form submitted')
        return True

    def service_get_name(self):
        try:
            self.page.wait_for_selector('#user-no-register', timeout=2000)
            self._pause('user not registered — about to dismiss')
            self.page.locator('button[ng-click="goLanding()"]').click()
            return False
        except PlaywrightTimeoutError:
            pass
        self._pause('about to read name')
        try:
            elem = self.page.locator('.contact_alias_ord')
            elem.wait_for()
            return elem.inner_text()
        except Exception as e:
            self.page.goto(MOVEMENTS_URL, wait_until="domcontentloaded")
            raise e

    def service_go_back(self):
        self._pause('about to go back')
        self.page.go_back()
        try:
            self.page.wait_for_load_state('domcontentloaded', timeout=10000)
        except Exception:
            pass
        try:
            self.page.locator('.contact__remove').wait_for(timeout=3000)
            self.page.locator('.contact__remove').click()
        except Exception as e:
            print(e, file=sys.stderr)
