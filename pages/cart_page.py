from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page:Page):
        self.page=page

        self.cart_items=page.locator(".cart_item")
        self.cart_item_names=page.locator(".inventory_item_name")
        self.cart_item_prices = page.locator(".inventory_item_price")
        self.checkout_button = page.locator("#checkout")
        self.page_title = page.locator(".title")

    def get_cart_item_count(self):
     expect(self.cart_items.first).to_be_visible()
     return self.cart_items.count()

    def get_cart_item_names(self):
       return self.cart_item_names.all_text_contents()

    def remove_cart_item_by_index(self, index):
       cart_item = self.cart_items.nth(index)
       cart_item.get_by_role("button", name="Remove").click()

    def remove_cart_item_by_name(self, name):
           cart_item = self.cart_items.filter(has_text=name)
           print("cart_item::",cart_item)
           cart_item.get_by_role("button", name="Remove").click()

    def get_cart_item_prices(self):
        prices = self.cart_item_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    def click_on_checkout(self):
        self.checkout_button.click()

    def get_page_title(self):
     return self.page_title

       
       
       

