from playwright.sync_api import sync_playwright
import pyautogui
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the first page
    page.goto("https://sso.gem.gov.in/ARXSSO/oauth/doLogin")
    time.sleep(5)

    # Perform actions on the first page
    # ...

    # Right-click on the captcha1 element using Playwright
    captcha_locator = page.locator("#captcha1")
    captcha_locator.click(button="right")

    # Sleep for 5 seconds (adjust as needed)
    time.sleep(9)

    # Get the bounding box information
    captcha_bounding_box = captcha_locator.bounding_box()

    if captcha_bounding_box:
        # Use PyAutoGUI to navigate to the desired context menu item
        captcha_position = captcha_bounding_box.get("viewport", captcha_bounding_box)
        pyautogui.moveTo(captcha_position["x"] + 10, captcha_position["y"] + 10)  # Adjust the offset as needed
        time.sleep(1)

        for _ in range(6):
            pyautogui.press("down")
            # time.sleep(1)

        # Emulate the keyboard press "Enter" to select the context menu item
        pyautogui.press("enter")

        # Sleep for 5 seconds (adjust as needed)
        time.sleep(5)
    else:
            print("Could not retrieve bounding box information for the captcha element.")
        # Access the pages property without calling it
    all_pages = context.pages

        # Check if the second page is present
    if len(all_pages) > 1:
            # Switch to the second tab (index 1 in Python, 2 in JavaScript)
            page1 = context.new_page()

            # Get the URL of the second page
            second_page_url = page1.url()
            print("Second Page URL:", second_page_url)

            # Perform actions on the second page
            captcha_element = page1.locator("div[jsname='JdLDjd'][class='hckaUb']").first()

            if captcha_element:
                captcha_value = captcha_element.inner_text()
                print("Captcha Value:", captcha_value)
            else:
                print("Element not found.")

            # Switch back to the first tab (index 0)
            context.page(0)

        

    # Perform other actions after interacting with the context menu
    time.sleep(13)

    context.close()
    browser.close()

with sync_playwright() as p:
    run(p)
