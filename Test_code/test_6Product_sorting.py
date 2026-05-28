from playwright.sync_api import sync_playwright

def test_product_sorting():

    with sync_playwright() as P:
        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Select sorting dropdown
        page.select_option(".product_sort_container", "lohi")        # lohi is the value for low to high sorting


        # Capture product prices
        prices = page.locator(".inventory_item_price").all_inner_texts()            # all_inner_texts() captures visible text from
                                                                                 # all matched elements and stores them into list format.
                                                                                    # example output = ['$29.99', '$9.99', '$15.99']
         # Empty list to store cleaned prices
        actual_prices = []

        # FOR Loop iterates through each product-price one by one.
        for price in prices:
            # Remove dollar symbol and convert string to float
            cleaned_price = float(price.replace("$", ""))               # output eg = 7.99


            # Store cleaned price into list
            actual_prices.append(cleaned_price)                                  # append() adds cleaned numeric value into actual_prices list.


        # Validation
        assert actual_prices == sorted(actual_prices), "Price sorting failed"

        # Take screenshot
        page.screenshot(path="Screenshots/product_sorting.png")

        # Close browser
        browser.close()