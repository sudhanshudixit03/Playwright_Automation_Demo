from playwright .sync_api import sync_playwright
def test_logout() :
    with sync_playwright () as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")


        #open side menu
        page.click("#react-burger-menu-btn")                    #react-burger-menu-btn is element ID.
                                                                # Hamburger Menu(☰)

        #click logout button
        page.click("#logout_sidebar_link")

        # Capture URL
        current_url = page.url

        # Validation
        assert current_url == "https://www.saucedemo.com/", "Logout failed"    #if logout is successful then it will redirect to the login page and the url will be "saucedemo.com"
                                                                          # but if logout is failed then it will not redirect to the login page and the url will be "saucedemo.com/inventory.html"

        # Screenshot
        page.screenshot(path="screenshots/logout.png")


        browser.close()