<img src="https://github.com/alejandrocora/bizleaker/raw/main/bizleaker.png" width="50px" height="50px" align="right">

[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
![Playwright](https://img.shields.io/badge/Playwright-1.x-blue.svg?logo=playwright&logoColor=white)
![Security](https://img.shields.io/badge/security-identity_check-blue)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-lightgray.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

# Bizleaker - Bizum Name Scraper

Bizleaker resolves phone numbers to names via the Bizum payment service. Given one or more numbers, it logs into your Santander account, runs each number through the Bizum send flow, and records the registered name — without completing any transaction.

Useful for verifying identities before responding to unknown numbers, flagging potential scams, or checking whether a contact is on Bizum before adding them.

<img src="https://github.com/alejandrocora/bizleaker/raw/main/screenshot.png">

---

## Requirements

- A **Santander** bank account with **Bizum** activated
- Python 3.9+

---

## 💻 Installation

```bash
git clone https://github.com/alejandrocora/bizleaker
cd bizleaker
pip3 install .
playwright install firefox chromium
```

---

## 📖 Usage

Look up a single number:

```bash
bizleaker +34600000000
```

Look up multiple numbers at once:

```bash
bizleaker +34600000000 +34611111111 +34622222222
```

Read numbers from a file, write results to another:

```bash
bizleaker --input numbers.txt --output results.txt
```

Use Chrome instead of Firefox, show the browser window:

```bash
bizleaker --chrome --visual +34600000000
```

Interactive mode (no numbers provided — prompts one by one):

```bash
bizleaker
```

---

## 🔧 Options

```
positional arguments:
  phones               Phone number or numbers (separated with blank spaces).

options:
  -h, --help           show this help message and exit
  --firefox            Use Firefox (default).
  --chrome             Use Chrome.
  --visual             Show browser UI.
  --id ID              Santander account ID (prompted if omitted).
  --password PASSWORD  Santander password (prompted if omitted).
  --input INPUT        Input file with phone numbers, one per line.
  --output OUTPUT      Output file to append results to.
  --debug              Pause at each automation phase for inspection.
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
