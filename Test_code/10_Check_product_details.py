from playwright .sync_api import sync_playwright
def test_check_product_details() :
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        #click on the first product
        page.click("#item_4_title_link")          #"item_4_title_link" is HTML element ID of the product "Sauce Labs Backpack"


        # Capture product details
        product_title = page.locator(".inventory_details_name").inner_text()    #inventory_details_name is class name of the product title

         #We can also use text_content() for direct text retrieval.
        # product_title = text_content(".inventory_details_name")



        # Validation
        assert product_title == "Sauce Labs Backpack", "Product details do not match"    #if the product title is "Sauce Labs Backpack" then it will pass the test but if the product title is not "Sauce Labs Backpack" then it will fail the test


        # Screenshot
        page.screenshot(path="screenshots/product_details.png")

        browser.close()
