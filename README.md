<img src="https://github.com/alejandrocora/bizleaker/raw/main/bizleaker.png" width="50px" height="50px" align="right">

[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.13.7-blue.svg)](https://www.python.org/)
![Selenium](https://img.shields.io/badge/Selenium-4.32.0-blue.svg?logo=selenium&logoColor=white)
![Security](https://img.shields.io/badge/security-identity_check-blue)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-lightgray.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

# Bizleaker - Bizum Name Scraper

Bizleaker automatically records name information (usually the first name and initials of surnames) from the Bizum service. It is designed to quickly check large numbers of phone numbers without a graphical interface, helping prevent scams, harassment, identity theft, or to identify a friend before adding them as a contact.

Many companies receive large volumes of messages and requests through SMS, chat apps, or phone calls, often trusting numbers blindly due to workload and urgency. This can lead to misdirected messages, information leaks, administrative errors, or financial scams. Bizleaker helps companies and individuals verify identities quickly and efficiently.

<img src="https://github.com/alejandrocora/bizleaker/raw/main/screenshot.png">

---

## ⚠️ Before Using

You will need a **WebDriver**, either **Firefox** or **Chrome**, depending on your preferred browser.

---

## 💻 Installation

```bash
git clone https://github.com/alejandrocora/bizleaker
cd bizleaker
pip3 install .
```

---

## 🆘 Usage / Help

Run the following for help:

```bash
bizleaker --help
```

Example output:

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

## ⚖️ Disclaimer

The author is **not responsible** for how this tool is used or for any errors it may cause.  
Use it at your own risk and always comply with **legal and privacy regulations**.  

This tool is **unofficial** and **not affiliated** with any services it interacts with.

---

## 👤 Author

**Alejandro Cora**  
<https://github.com/alejandrocora>
