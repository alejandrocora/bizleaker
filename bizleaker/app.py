#!/usr/bin/env python3

# Bizleaker

import os
import getpass
import argparse
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bizleaker.utils.santander import Santander
from bizleaker.utils.selaux import *


def get_name(driver, account, number, output):
    if output:
        output = open(output, 'a')
    try:
        account.service_send(number)
        name = account.service_get_name()
        text = '[+] ' + number + ' -> ' + name
        if not output:
            print(text)
        driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        print('[!] Unable to get ' + number + '.')
    if output:
        output.write(text + '\n')
        output.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', default=False, action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', action='store_true', help='Use Chrome.')
    parser.add_argument('--id', dest='id', help='ID number for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')
    parser.add_argument('--input', dest='input', help='Input file with the phone numbers list divided in lines.')
    parser.add_argument('--output', dest='output', default=False, help='Output file to store results.')
    parser.add_argument('phones',  metavar='phones', type=str, nargs='+', help='Phone number or numbers (separated with blank spaces).')
    args = parser.parse_args()
    id = args.id
    password = args.password
    browser = args.browser
    output = args.output
    execution_mode = 1
    if not args.input:
        if args.phones:
            phones = args.phones
        else:
            execution_mode = 0
    else:
        with open(args.input, 'r') as f:
            phones = f.read().splitlines()
    if not id:
        id = input('Account ID: ')
    if not password:
        password = getpass.getpass('Account password: ')
    if browser:
        driver = headless_chrome()
    else:
        driver = headless_firefox()
    account = Santander(driver, id)
    try:
        account.login(password)
    except Exception as e:
        print('[!] Unable to log in.')
        return e
    print('[i] Logged in successfully.')
    account.open_service()
    if execution_mode == 1:
        for number in phones:
            number = number.replace(' ', '')
            get_name(driver, account, number, output)
    else:
        number = input('[*] Phone number (Press [ENTER] to finish): ')
        while number:
            get_name(driver, account, number.replace(' ', ''), output)
            number = input('[*] Phone number (Press [ENTER] to finish): ')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()


if __name__ == '__main__':
    main()
