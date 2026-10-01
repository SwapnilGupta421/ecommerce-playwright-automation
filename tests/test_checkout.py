import pytest
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInformationPage, CheckoutOverviewPage,CheckoutCompletePage
from playwright.sync_api import Page, expect

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("first_name,last_name,code",[("Sweety","Gupta","474001"),("Swapnil","Gupta","560091")])
def test_form_validation_on_checkout(login_page,first_name,last_name,code):
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page=CartPage(products_page.page)
    cart_page.click_on_checkout()

    Chkout_page=CheckoutInformationPage(cart_page.page)
    Chkout_page.update_firstname(first_name)
    Chkout_page.update_lastname(last_name)
    Chkout_page.update_zipcode(code)

    actual_firstname = Chkout_page.get_firstname()
    actual_lastname = Chkout_page.get_lastname()
    actual_zipcode = Chkout_page.get_zipcode()

    print("\n")
    print("======================================")

    assert Chkout_page.get_page_title() == "Checkout: Your Information"

    print(f"First Name | Expected: {first_name} | Actual: {actual_firstname}")
    print(f"Last Name  | Expected: {last_name} | Actual: {actual_lastname}")
    print(f"Code       | Expected: {code} | Actual: {actual_zipcode}")

    assert actual_firstname == first_name, (
    f"First Name FAILED | Expected: {first_name} | Actual: {actual_firstname}"
    )


    assert actual_lastname == last_name, (
    f"Last Name FAILED | Expected: {last_name} | Actual: {actual_lastname}"
    )


    assert actual_zipcode == code, (
    f"Code FAILED | Expected: {code} | Actual: {actual_zipcode}"
    )
@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_overview_page_validation(login_page):
        login_page.open()
        login_page.login("standard_user","secret_sauce")
    
        products_page = ProductsPage(login_page.page)
        products_page.add_all_products_to_cart()
        prices=products_page.get_all_product_prices()
        products_page.open_cart()
    
        cart_page=CartPage(products_page.page)
        cart_page.click_on_checkout()
    
        checkout_page1=CheckoutInformationPage(cart_page.page)
        checkout_page1.update_firstname("Sweety")
        checkout_page1.update_lastname("Gupta")
        checkout_page1.update_zipcode("123456789")
        checkout_page1.click_on_continue()

        checkout_page2=CheckoutOverviewPage(checkout_page1.page)

        checkout_page2.wait_for_page()

        assert checkout_page2.get_page_title()=="Checkout: Overview"

        expect(checkout_page1.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
            )

        

        assert checkout_page2.get_payment_label()=="Payment Information:"
        expect(checkout_page2.payment_info_value).to_contain_text("SauceCard #")
        
        assert checkout_page2.get_shipping_label()=="Shipping Information:"
        assert checkout_page2.get_shipping_info_value()=="Free Pony Express Delivery!"
        assert checkout_page2.get_price_total_label()=="Price Total"
        expect(checkout_page2.price_total_info_value).to_have_text("Item total: $"+str(sum(prices)))
        tax=float(checkout_page2.get_tax().replace("$","").replace("Tax: ",""))
        print("Actual: Total: $"+str(sum(prices)+tax))
        print("Expected: "+checkout_page2.get_total_with_tax())
        expect(checkout_page2.total_with_tax).to_have_text("Total: $"+str(sum(prices)+tax))

        checkout_page2.click_on_finish_btton()

        expect(checkout_page2.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_complete_page_validation(login_page):
        login_page.open()
        login_page.login("standard_user","secret_sauce")
    
        products_page = ProductsPage(login_page.page)
        products_page.add_all_products_to_cart()
        products_page.open_cart()
    
        cart_page=CartPage(products_page.page)
        cart_page.click_on_checkout()
    
        checkout_page1=CheckoutInformationPage(cart_page.page)
        checkout_page1.update_firstname("Sweety")
        checkout_page1.update_lastname("Gupta")
        checkout_page1.update_zipcode("123456789")
        checkout_page1.click_on_continue()


        checkout_page2=CheckoutOverviewPage(checkout_page1.page)
        checkout_page2.click_on_finish_btton()

        checkout_page3=CheckoutCompletePage(checkout_page2.page)
        assert checkout_page3.get_complete_header()=="Thank you for your order!"
        assert checkout_page3.get_complete_text()=="Your order has been dispatched, and will arrive just as fast as the pony can get there!"

        checkout_page3.click_on_back_to_home()
        expect(checkout_page3.page).to_have_url("https://www.saucedemo.com/inventory.html")


        



        

        

        


