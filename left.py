from playwright.sync_api import sync_playwright
import time

def run(playwright):
    # Launch Firefox browser
    browser = playwright.firefox.launch(headless=False)
    
    # Create a new context and page
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the login page
    page.goto("https://lens.google.com/search?ep=cnts&re=df&s=4&p=AbrfA8ofSTbAszdvgUNf_leVi9GlYp7HdM0X62xDe6bf5PR1XtYIF3O3sPp5dVGFw_dXqOM5OaCdLU5JxrdXm2Rur3rtNbPmmUV8JkktiBMXqOMKw8rkLODj4QA__ATYCX1lc1sJHdtaUZcojKeGBWxWzZhvEDwgraIElvzgaXqCJsO72O7Nc0nRfB5eKyO9XEFrSflKaJb5HXF2xWEmAutF6EfaKJKe3hLTOQdxSeoadCL7UN5JhoiIn3QZk8_uEEQAcp568NMCG5lgPAq91PF0UJOabmqKT7QiPHqXVqAPfMH8yuRp0wkyKijk-Xh3VR5zGHk821EkTA%3D%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKREExTVRrNU1HSmtMVFJsTTJZdE5HSTBZeTA0WTJNeExUSmtNMk0xWkdOaVpqTXhOUklmU1RnNVdHaFpYM1JyTWxsVk9FZHRjM3A0VFdaRGJITnVNRWxmTXpCb1p3PT0iLG51bGwsbnVsbCxudWxsLDEsbnVsbCxbbnVsbCxudWxsLG51bGwsW1s0MzUwMCw1OTk5N11dXV0=")
    
    # Sleep for 5 seconds
    time.sleep(5)

    # Find the element using the provided jsname and class
    captcha_element = page.query_selector("div[jsname='JdLDjd'][class='hckaUb']")

    if captcha_element:
        captcha_value = captcha_element.inner_text()
        print("Captcha Value:", captcha_value)
    else:
        print("Element not found.")

    # Close the browser
    browser.close()

with sync_playwright() as p:
    run(p)
