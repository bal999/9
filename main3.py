from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sso.gem.gov.in/ARXSSO/oauth/doLogin")
    time.sleep(5)
    # Right-click on the captcha1 element
    captcha_locator = page.locator("#captcha1")
    captcha_locator.click(button="right")
    time.sleep(5)
    # Emulate pressing the "ArrowDown" key multiple times
    for _ in range(6):
        page.keyboard.press("ArrowDown")

    # Emulate the keyboard press "Enter" to select the context menu item
    page.keyboard.press("Enter")
    time.sleep(5)
    # Continue with other actions if needed

    context.close()
    browser.close()

with sync_playwright() as p:
    run(p)
