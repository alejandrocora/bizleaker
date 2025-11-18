<img src="https://github.com/alejandrocora/ghostgram/blob/main/images/bizleaker.png?raw=true" width="50px" height="50px" align="right">

[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.13.7-blue.svg)](https://www.python.org/)
![Selenium](https://img.shields.io/badge/Selenium-4.32.0-blue.svg?logo=selenium&logoColor=white)
![Security](https://img.shields.io/badge/security-identity_check-blue)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-lightgray.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

# Bizleaker - Bizum Name Scraper

Bizleaker records name (usually name and the initials of the surnames) information from the Bizum service automatically. The purpose of the tool is to check large amounts of telephone numbers quickly without graphical interface, to prevent scam, harassment, identity theft or to simply identify a friend before adding him as a contact.

Plenty of companies receive tons of petititons and messages through SMS, chat applications or phone calls through numbers they usually blindly trust because of the large volume of contacts they must attend to and the urgency of their tasks. In many cases, this ends up with many problems, messages that were intented to a different contact, confussions, information leaks, administrative errors or the worst of all (although not uncommon) money scams.

Bizleaker helps companies and individuals to check the identity of these numbers in a quick and easy way to prevent these types of problems. Bizleaker does not access in any illegal way to this information or to any service.

<img src="https://github.com/alejandrocora/bizleaker/blob/main/images/screenshot.png?raw=true">

---

## Before using it

You will need to install a **WebDriver**, either **Firefox** or **Chrome**, depending on which browser you plan to use.

---

## Installation

`$ git clone https://github.com/alejandrocora/bizleaker`  
`$ cd bizleaker`  
`$ pip3 install .`

---

## Help

Run `bizleaker --help` for help:
```
usage: bizleaker [-h] [--firefox] [--chrome] [--visual] [--id ID] [--password PASSWORD]
                 [--input INPUT] [--output OUTPUT]
                 [phones ...]

positional arguments:
  phones               Phone number or numbers (separated with blank spaces).

options:
  -h, --help           show this help message and exit
  --firefox            Use Firefox.
  --chrome             Use Chrome.
  --visual             Show browser UI.
  --id ID              ID number for login.
  --password PASSWORD  Password for login.
  --input INPUT        Input file with the phone numbers list divided in lines.
  --output OUTPUT      Output file to store results.

```

---

### Disclaimer

The author is **not responsible** for the use of this tool or for any type of error it may cause.  
Use it at your own risk and always follow **legal and privacy requirements**.  

This tool is **not official** and **not related** to any of the services it interacts with.

---

## Author

**Alejandro Cora**  
<https://github.com/alejandrocora>
