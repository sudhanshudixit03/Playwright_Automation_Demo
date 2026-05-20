from playwright .sync_api import sync_playwright
def test_product_sorting():
    with sync_playwright() as P:
        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        #LOGIN
        page.fill("#user-name","standard_user")
        page.fill("#password","secret_sauce")
        page.click("#login-button")

        #ADD TO CART
        page.click("#add-to-cart-sauce-labs-backpack")

        #OPEN CART
        page.click(".shopping_cart_link")

        # Click checkout button
        page.click("#checkout")

        #enter first and last name
        page.fill("#first-name","SUDHANSHU")
        page.fill("#last-name","DIXIT")

        #Enter zip code
        page.fill("#postal-code","209801")

        #click continue
        page.click("#continue")

        #Finish
        page.click("#finish")

        #validation
        assert page.locator(".complete-header").inner_text() == "Thank you for your order!"

        page.screenshot(path="Screenshots/verify_checkout.png")

        browser.close()
