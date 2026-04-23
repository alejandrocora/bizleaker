#!/usr/bin/env python3

# Bizleaker

import sys
import argparse
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError

from bizleaker.utils.selaux import chrome, firefox
from bizleaker.utils.constants import *
from bizleaker.utils.santander import Santander


def getpass_asterisk(prompt='Account password: '):
    print(prompt, end='', flush=True)
    if sys.platform == 'win32':
        import msvcrt
        password = ''
        while True:
            ch = msvcrt.getwch()
            if ch in ('\r', '\n'):
                break
            elif ch == '\x03':
                raise KeyboardInterrupt
            elif ch == '\x08':
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            else:
                password += ch
                print('*', end='', flush=True)
        print()
        return password
    else:
        import tty, termios
        password = ''
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in ('\r', '\n'):
                    break
                elif ch == '\x7f':
                    if password:
                        password = password[:-1]
                        print('\b \b', end='', flush=True)
                elif ch == '\x03':
                    raise KeyboardInterrupt
                else:
                    password += ch
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        print()
        return password


def get_name(account, number, output):
    try:
        if not account.service_send(number):
            return False
        name = account.service_get_name()
        if not name:
            print('[!] ' + number + ' is not registered on ' + SERVICE_NAME + '.')
            return False
        text = '[+] ' + number + ' -> ' + name
        print(text)
        if output:
            output.write(text + '\n')
    except (PlaywrightTimeoutError, PlaywrightError):
        print('[!] Unable to get ' + number + '.')
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--firefox', dest='browser', default=False, action='store_false', help='Use Firefox (default).')
    parser.add_argument('--chrome', dest='browser', action='store_true', help='Use Chrome.')
    parser.add_argument('--visual', dest='headless', default=True, action='store_false', help='Show browser UI.')
    parser.add_argument('--id', dest='id', help='Santander account ID (prompted if omitted).')
    parser.add_argument('--password', dest='password', help='Santander password (prompted if omitted).')
    parser.add_argument('--input', dest='input', help='Input file with phone numbers, one per line.')
    parser.add_argument('--output', dest='output', default=None, help='Output file to append results to.')
    parser.add_argument('--debug', dest='debug', default=False, action='store_true', help='Pause at each automation phase for inspection.')
    parser.add_argument('phones', metavar='phones', type=str, nargs='*', help='Phone number or numbers (separated with blank spaces).')
    args = parser.parse_args()
    id = args.id
    password = args.password
    browser = args.browser
    headless = args.headless
    debug = args.debug
    execution_mode = 1
    pw = None
    bw = None
    output = None
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
            password = getpass_asterisk()
        if args.output:
            output = open(args.output, 'a')
        if browser:
            pw, bw, context, page = chrome(headless=headless)
        else:
            pw, bw, context, page = firefox(headless=headless)
        account = Santander(page, context, id, debug=debug)
        try:
            print('[i] Logging in....')
            account.login(password)
        except Exception as e:
            print('[!] Unable to log in.')
            return e
        print('[i] Logged in successfully.')
        if debug:
            input('[DEBUG] logged in — press ENTER to continue...')
        print('[i] Opening ' + SERVICE_NAME + ' service...')
        account.open_service()
        print('[i] ' + SERVICE_NAME + ' opened successfully.')
        if debug:
            input('[DEBUG] service opened — press ENTER to continue...')
        if execution_mode == 1:
            for number in phones:
                number = number.replace(' ', '')
                if get_name(account, number, output):
                    account.service_go_back()
        else:
            while True:
                number = input('[*] Phone number (Press [ENTER] to finish): ').strip()
                if not number:
                    break
                if get_name(account, number.replace(' ', ''), output):
                    account.service_go_back()
    except Exception as e:
        print(e)
    finally:
        if output:
            output.close()
        if bw:
            try:
                bw.close()
            except Exception:
                pass
        if pw:
            try:
                pw.stop()
            except Exception:
                pass


if __name__ == '__main__':
    main()
