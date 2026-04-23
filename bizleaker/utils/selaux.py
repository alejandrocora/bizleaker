from playwright.sync_api import sync_playwright


def chrome(headless=True):
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=headless)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
        viewport={"width": 1280, "height": 800}
    )
    context.set_default_timeout(60000)
    page = context.new_page()
    return pw, browser, context, page


def firefox(headless=True):
    pw = sync_playwright().start()
    browser = pw.firefox.launch(headless=headless)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
        viewport={"width": 1280, "height": 800}
    )
    context.set_default_timeout(60000)
    page = context.new_page()
    return pw, browser, context, page
