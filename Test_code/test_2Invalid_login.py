from playwright.sync_api import sync_playwright
def test_invalid_login():
      with sync_playwright() as p:
            browser=p.chromium.launch(headless=False)
            page=browser.new_page()
            page.goto("https://www.saucedemo.com/")             #1st step
            page.fill("#user-name","student_123")
            page.fill("#password","sauce_incorrect")
            page.click("#login-button")
            # assert page.locator("h3").inner_text() == "Epic sadface: Username and password do not match any user in this service"
            assert "Epic sadface" in page.locator("h3").inner_text()
            page.screenshot(path="Screenshots/screenshot1.png")
            print("Login unsuccessful")
            browser.close()






