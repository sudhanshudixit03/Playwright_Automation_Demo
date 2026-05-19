from playwright.sync_api import sync_playwright
def test_remove_cart_item():
    with sync_playwright() as P:
        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        #LOGIN
        page.fill("#user-name","standard_user")
        page.fill("#password","secret_sauce")
        page.click("#login-button")

        #add product to cart
        page.click("#add-to-cart-sauce-labs-backpack")

        #open cart
        page.click(".shopping_cart_link")

        #remove product from cart
        page.click("#remove-sauce-labs-backpack")

        #validation /cart "badge" disappears
        assert page.locator(".shopping_cart_badge").count() == 0


        page.screenshot(path="Screenshots/screenshot4.png")
        browser.close()