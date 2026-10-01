import pytest
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.product_page import ProductsPage

@pytest.mark.smoke
def test_cart_items(login_page):
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    products_page = ProductsPage(login_page.page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    

    cart_page = CartPage(products_page.page)

    assert cart_page.get_cart_item_count() == 1

    assert "Sauce Labs Backpack" in cart_page.get_cart_item_names()

@pytest.mark.regression
def test_cart_add_all_items(login_page):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(login_page.page)

        products_names =products_page.add_all_products_to_cart()
        products_page.open_cart()

        cart_page = CartPage(products_page.page)

        cart_names=cart_page.get_cart_item_names()

        assert cart_page.get_cart_item_count() == len(products_names)

        assert products_names == cart_names

@pytest.mark.regression
@pytest.mark.parametrize("index", [2, 4])
def test_cart_remove_by_index(login_page,index):
      login_page.open()
      login_page.login("standard_user", "secret_sauce")
      products_page = ProductsPage(login_page.page)
      products_names =products_page.add_all_products_to_cart()
      products_page.open_cart()
      cart_page = CartPage(products_page.page)
      cart_page.remove_cart_item_by_index(index)

      assert cart_page.get_cart_item_count() == 5

      cart_names=cart_page.get_cart_item_names()
      print("cart_names",cart_names)

      products_names.pop(index)

      print("products_names",products_names)

      assert cart_names == products_names

@pytest.mark.regression
@pytest.mark.parametrize("item_name", ['Sauce Labs Bolt T-Shirt'])
def test_cart_removed_by_name(login_page, item_name):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(login_page.page)
        products_names =products_page.add_all_products_to_cart()
        products_page.open_cart()
        cart_page = CartPage(products_page.page)
        cart_page.remove_cart_item_by_name(item_name)
        assert cart_page.get_cart_item_count() == 5
        cart_names=cart_page.get_cart_item_names()
        print("cart_names",cart_names)
        products_names.remove(item_name)
        print("products_names",products_names)
        assert cart_names == products_names

@pytest.mark.regression
@pytest.mark.parametrize(
    "item_names",
    [
        [
            "Sauce Labs Bolt T-Shirt"
        ],
        [
            "Sauce Labs Fleece Jacket"
        ],
        [
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket"
        ],
        [
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Bike Light",
            "Sauce Labs Backpack"
        ]
    ]
)
def test_cart_total_matches_selected_product_prices(login_page,item_names):
       login_page.open()
       login_page.login("standard_user", "secret_sauce")
       products_page = ProductsPage(login_page.page)
       prices=products_page.add_products_to_cart_by_name(item_names)
       expected_total =sum(prices)
       products_page.open_cart()
       cart_page=CartPage(products_page.page)
       actual_total=sum(cart_page.get_cart_item_prices())
       assert actual_total == expected_total

@pytest.mark.regression
@pytest.mark.parametrize(
    "item_names",
    [
            ["Sauce Labs Bolt T-Shirt",
             "Sauce Labs Fleece Jacket",
             "Sauce Labs Bike Light",
             "Sauce Labs Backpack"],
            ["Sauce Labs Bolt T-Shirt",
             "Sauce Labs Fleece Jacket"],
    ]
)
def test_cart_quantity_validation(login_page,item_names):
       login_page.open()
       login_page.login("standard_user", "secret_sauce")
       products_page = ProductsPage(login_page.page)
       products_page.add_products_to_cart_by_name(item_names)

       expect_quantity=int(products_page.get_cart_count().inner_text())
       products_page.open_cart()
       cart_page=CartPage(products_page.page)
       actual_count=cart_page.get_cart_item_count()
       assert actual_count==expect_quantity





       

      

      

      

        





