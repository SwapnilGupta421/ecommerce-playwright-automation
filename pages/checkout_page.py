from playwright.sync_api import Page


class CheckoutInformationPage:
    def __init__(self, page: Page):
        self.page=page
        self.firstname=page.locator('[placeholder="First Name"]')
        self.lastname=page.locator('[placeholder="Last Name"]')
        self.zipcode=page.locator('[placeholder="Zip/Postal Code"]')
        self.continue_btn=page.locator('#continue')
        self.cancel_btn=page.locator('#cancel')
        self.page_title = page.locator(".title")
        

    def update_firstname(self,value):
        self.firstname.fill(value)

    def update_lastname(self,value):
            self.lastname.fill(value)

    def update_zipcode(self,value):
            self.zipcode.fill(value)

    def get_firstname(self):
          return self.firstname.input_value()
    
    def get_lastname(self):
              return self.lastname.input_value()
    
    def get_zipcode(self):
              return self.zipcode.input_value()

    def click_on_continue(self):
           self.continue_btn.click()

    def click_on_cancel(self):
           self.cancel_btn.click()

    def get_page_title(self):
           return self.page_title.inner_text()


class CheckoutOverviewPage:
       def __init__(self,page:Page):
              self.page=page
              self.payment_label=page.locator('[data-test="payment-info-label"]')
              self.shipping_label=page.locator('[data-test="shipping-info-label"]')
              self.payment_info_value=page.locator('[data-test="payment-info-value"]')
              self.shipping_info_value=page.locator('[data-test="shipping-info-value"]')
              self.price_total_label=page.locator('[data-test="total-info-label"]')
              self.price_total_info_value=page.locator('[data-test="subtotal-label"]')
              self.tax=page.locator('[data-test="tax-label"]')
              self.total_with_tax=page.locator('[data-test="total-label"]')
              self.finish_btn=page.locator('#finish')


       def get_payment_label(self):
               return self.payment_label.inner_text()

       def get_shipping_label(self):
              return self.shipping_label.inner_text()

       def get_payment_info_value(self):
              return self.payment_info_value.inner_text()

       def get_shipping_info_value(self):
              return self.shipping_info_value.inner_text()

       def get_price_total_label(self):
              return self.price_total_label.inner_text()

       def get_price_total_info_value(self):
              return self.price_total_info_value.inner_text()

       def get_tax(self):
              return self.tax.inner_text()

       def get_total_with_tax(self):
              return self.total_with_tax.inner_text()

       def click_on_finish_btton(self):
              return self.finish_btn.click()



class CheckoutCompletePage:
       def __init__(self,page:Page):
              self.page=page
              self.complete_header=page.locator('.complete-header')
              self.complete_text=page.locator('.complete-text')
              self.back_to_home=page.locator('#back-to-products')


       def get_complete_header(self):
              return self.complete_header.inner_text()

       def get_complete_text(self):
              return self.complete_text.inner_text()

       def click_on_back_to_home(self):
              self.back_to_home.click()




              
           
























