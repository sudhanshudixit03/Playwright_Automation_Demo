from playwright .sync_api import sync_playwright
def test_add_more_product_cart():
    with sync_playwright() as P:
        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        #LOGIN
        page.fill("#user-name","standard_user")
        page.fill("#password","secret_sauce")
        page.click("#login-button")

        #add more product to cart
        page.click("#add-to-cart-sauce-labs-bike-light")
        page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        page.click("#add-to-cart-sauce-labs-fleece-jacket")
        page.click("#add-to-cart-sauce-labs-onesie")

        #open cart
        page.click(".shopping_cart_link")

        #validation
        assert page.locator("#shopping_cart_container").inner_text() == "4"

        page .screenshot(path="Screenshots/screenshot3.png")
        browser.close()
