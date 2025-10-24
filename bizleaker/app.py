#!/usr/bin/env python3

# Bizleaker

import getpass
import argparse
from time import sleep
from selenium.common.exceptions import *

from bizleaker.utils.selaux import *
from bizleaker.utils.constants import *
from bizleaker.utils.santander import Santander


def get_name(account, number, output):
    if output:
        output = open(output, 'a')
    try:
        if not account.service_send(number):
            return False
        name = account.service_get_name()
        if not name:
            print('[!] ' + number + ' is not registered on ' + SERVICE_NAME + '.')
            return False
        text = '[+] ' + number + ' -> ' + name
        if not output:
            print(text)
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        print('[!] Unable to get ' + number + '.')
        return False
    if output:
        output.write(text + '\n')
        output.close()
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', default=False, action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', action='store_true', help='Use Chrome.')
    parser.add_argument('--visual', dest='headless', default=True, action='store_false', help='Show browser UI.')
    parser.add_argument('--id', dest='id', help='ID number for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')
    parser.add_argument('--input', dest='input', help='Input file with the phone numbers list divided in lines.')
    parser.add_argument('--output', dest='output', default=False, help='Output file to store results.')
    parser.add_argument('phones',  metavar='phones', type=str, nargs='*', help='Phone number or numbers (separated with blank spaces).')
    args = parser.parse_args()
    id = args.id
    password = args.password
    browser = args.browser
    headless = args.headless
    output = args.output
    execution_mode = 1
    try:
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
            driver = chrome(headless=headless)
        else:
            driver = firefox(headless=headless)
        account = Santander(driver, id)
        try:
            print('[i] Logging in....')
            account.login(password)
        except Exception as e:
            print('[!] Unable to log in.')
            return e
        print('[i] Logged in successfully.')
        print('[i] Opening ' + SERVICE_NAME + ' service...')
        account.open_service()
        print('[i] ' + SERVICE_NAME + ' opened successfully.')
        if execution_mode == 1:
            for number in phones:
                number = number.replace(' ', '')
                if get_name(account, number.replace(' ', ''), output):
                    account.service_go_back()
        else:
            while True:
                number = input('[*] Phone number (Press [ENTER] to finish): ').strip()
                if not number:
                    break
                if get_name(account, number.replace(' ', ''), output):
                    account.service_go_back()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
    except Exception as e:
        print(e)
        if headless:
            driver.close()


if __name__ == '__main__':
    main()