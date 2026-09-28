from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.products_title = page.locator(".title")
        self.product_items = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.backpack_add_button = page.locator(
                    "#add-to-cart-sauce-labs-backpack"
                )
        
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_page_title(self):
        return self.products_title

    def get_product_count(self):
        return self.product_items.count()

    def get_product_names(self):
            return self.product_names.all_text_contents()
    
    def add_backpack_to_cart(self):
            self.backpack_add_button.click()
    
    def get_cart_count(self):
            return self.cart_badge

    def open_cart(self):
          self.page.locator(".shopping_cart_link").click()

    def add_all_products_to_cart(self):
        products = self.page.locator(".inventory_item")
        names = []

        for i in range(products.count()):
            product = products.nth(i)
            name = product.locator(".inventory_item_name").inner_text()
            print("Adding:", name)
            names.append(name)
            product.get_by_role("button", name="Add to cart").click()

        return names

    def add_product_to_cart_by_name(self,name):
         product_item = self.product_items.filter(has_text=name)
         print("product_item added to the cart:",product_item)
         product_item.get_by_role("button", name="Add to cart").click()
         price=product_item.locator(".inventory_item_price").inner_text()
         return float(price.replace("$", ""))

    def add_products_to_cart_by_name(self,names):
         prices=[]
         for item_name in names:
              price=self.add_product_to_cart_by_name(item_name)
              prices.append(price)
         return prices

    def remove_product_by_name(self,name):
         product_item = self.product_items.filter(has_text=name)
         print("product_item removed from the cart:",product_item)
         product_item.get_by_role("button",name="remove").click()

    def get_all_product_prices(self):
        products = self.page.locator(".inventory_item")
        prices = []

        for i in range(products.count()):
            product = products.nth(i)

            price = float(
                product.locator(".inventory_item_price")
                .inner_text()
                .replace("$", "")
            )

            prices.append(price)

        return prices



         
         


          