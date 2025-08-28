import re
from playwright.sync_api import Page, expect


def test_search_product(page: Page):
    # Test data
    search_item = "hammer"
    quantity = "3"

    # Open the page
    page.goto("https://practicesoftwaretesting.com/")
    
    # Search for product
    page.locator("[data-test=search-query]").fill(search_item)
    page.locator("[data-test=search-submit]").click()

    # Sort by Price (High - Low)
    page.locator("[data-test=sort]").select_option("price,desc")

    # Open first product from the list
    first_product = page.locator("[data-test^=product-]").first
    first_product.click()

    # Save product details
    product_name = page.locator("[data-test=product-name]").inner_text()
    product_price = page.locator("[data-test=unit-price]").inner_text()


    page.locator("[data-test=\"product-name\"]").click()
    page.locator("[data-test=\"unit-price\"]").click()

    # Enter quantity and add to cart
    page.locator("[data-test=quantity]").fill(quantity)
    page.locator("[data-test=add-to-cart]").click()
    

    # Go to cart
    page.locator("[data-test=nav-cart]").click()

    # Assertions
    expect(page.locator("[data-test=product-title]")).to_have_text(product_name)
    expect(page.locator("[data-test=product-quantity]")).to_have_value(quantity)
    expect(page.locator("[data-test=product-price]")).to_contain_text(product_price)
