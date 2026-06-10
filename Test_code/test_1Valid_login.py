from playwright.sync_api import sync_playwright
def test_valid_login():
      with sync_playwright() as p:
            browser=p.chromium.launch(headless=False)
            page=browser.new_page()

            page.goto("https://www.saucedemo.com/")             #1st step
            page.fill("#user-name","standard_user")     #instead of css selectors we can also "use get_by_label"
            page.fill("#password","secret_sauce")
            page.click("#login-button")
            # assert page.locator(".title").inner_text() == 'Products'
            assert "Products" in page.locator(".title").inner_text()
            page.screenshot(path="Screenshots/login.png")
            print("Login successful")
            browser.close()




