from playwright.sync_api import sync_playwright

def test_add_single_product_cart():

    with sync_playwright() as P:

        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        #LOGIN
        page.fill("#user-name","standard_user")
        page.fill("#password","secret_sauce")
        page.click("#login-button")

        #add single product to cart
        page.click("#add-to-cart-sauce-labs-backpack")

        #open cart
        page.click(".shopping_cart_link")               #Dot(.) represents class selector in CSS.
                                                                #shopping_cart_link is class name.

        #validation
        assert page.locator("#shopping_cart_container").inner_text() == "1"

        page.screenshot(path="Screenshots/screenshot2.png")
        browser .close()
