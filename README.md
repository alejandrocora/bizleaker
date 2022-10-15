# Bizleaker - Bizum Name Scraper

Bizleaker records name (usually name and the initials of the surnames) information from Bizum automatically. The purpose of the tool is to check large amounts of telephone numbers quickly without graphical interface, to prevent scam, harassment, identity theft or to simply identify a friend before adding him as a contact. It is not intended for any criminal or wrongful use.

## Before using it...

For now, a Santander account is necessary to use it, introducing your ID and password. You will also need to install a Web Driver, be it Firefox or Chrome. If you need help to install the latter, click [here](https://github.com/alejandrocora/install_webdriver "Install Webdriver").

## Installation

`$ git clone https://github.com/alejandrocora/bizleak`  
`$ cd bizleak`  
`$ pip3 install .`

## Help

Run `bizleaker --help` for help:
```
usage: bizleaker [-h] [--firefox] [--chrome] [--id ID] [--password PASSWORD]
              [--phones PHONES] [--input INPUT] [--output OUTPUT]

options:
  -h, --help           show this help message and exit
  --firefox            Use Firefox.
  --chrome             Use Chrome.
  --id ID              ID number for login.
  --password PASSWORD  Password for login.
  --phones PHONES      Phone numbers list divided by commas.
  --input INPUT        Input file with the phone numbers list divided by lines.
  --output OUTPUT      Output file to store results.
```

### Disclaimer

Author is not responsible for its use or any type of error it may lead. Use it at your own risk.
