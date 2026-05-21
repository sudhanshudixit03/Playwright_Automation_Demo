from playwright .sync_api import sync_playwright
def test_empty_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Open cart without adding product
        page.click(".shopping_cart_link")

        #click checkout button
        page.click("#checkout")

        # enter first and last name
        page.fill("#first-name", "SUDHANSHU")
        page.fill("#last-name", "DIXIT")
        page.fill("#postal-code", "209801")

        # click continue
        page.click("#continue")

        # Capture URL
        current_url = page.url

        # Validation
        assert "checkout-step-two" in current_url, "Checkout page not opened"    #"checkout-step-two" means it will try to open the checkout page(current_url)
                                                                                # but it should not open because there is no product in the cart

        # Screenshot
        page.screenshot(path="screenshots/empty_cart_checkout.png")

        browser.close()

