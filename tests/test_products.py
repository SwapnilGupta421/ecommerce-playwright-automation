import pytest
from playwright.sync_api import expect
from pages.product_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_products_are_displayed(login_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page = ProductsPage(login_page.page)

    expect(products_page.get_page_title()).to_have_text("Products")

    assert products_page.get_product_count() == 6

    product_names = products_page.get_product_names()

    assert "Sauce Labs Backpack" in product_names

@pytest.mark.smoke
def test_add_backpack_to_cart(login_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_backpack_to_cart()

    expect(products_page.get_cart_count()).to_have_text("1")

@pytest.mark.regression
@pytest.mark.parametrize("item_name", ['Sauce Labs Bolt T-Shirt','Sauce Labs Fleece Jacket'])
def test_add_product_to_cart_by_name(login_page, item_name):
    login_page.open()
    login_page.login(
            "standard_user",
            "secret_sauce"
        )
    products_page = ProductsPage(login_page.page)
    products_page.add_product_to_cart_by_name(item_name)

    products_page.open_cart()
    cart_page = CartPage(products_page.page)
    print(cart_page.get_cart_item_names())
    assert cart_page.get_cart_item_count()==1
    assert cart_page.get_cart_item_names() == [item_name]

@pytest.mark.regression
def test_add_products_to_cart_by_name(login_page):
    login_page.open()
    login_page.login(
                "standard_user",
                "secret_sauce"
            )
    products_page = ProductsPage(login_page.page)

    item_names=['Sauce Labs Bolt T-Shirt','Sauce Labs Fleece Jacket']
    products_page.add_products_to_cart_by_name(item_names)
    products_page.open_cart()
    cart_page = CartPage(products_page.page)
    assert cart_page.get_cart_item_count()==len(item_names)
    assert cart_page.get_cart_item_names() == item_names
@pytest.mark.regression
@pytest.mark.parametrize(
    "item_names, removed_item",
    [
        (
            ["Sauce Labs Bolt T-Shirt",
             "Sauce Labs Fleece Jacket",
             "Sauce Labs Bike Light",
             "Sauce Labs Backpack"],
            ["Sauce Labs Bike Light"]
        ),
        (
            ["Sauce Labs Bolt T-Shirt",
             "Sauce Labs Fleece Jacket",
             "Sauce Labs Bike Light",
             "Sauce Labs Backpack"],
            ["Sauce Labs Fleece Jacket","Sauce Labs Bolt T-Shirt"]
        )
    ]
)
def test_remove_product_by_name(login_page,item_names,removed_item):
    login_page.open()
    login_page.login(
                "standard_user",
                "secret_sauce"
            )
    products_page = ProductsPage(login_page.page)

    products_page.add_products_to_cart_by_name(item_names)

    expect(products_page.get_cart_count()).to_have_text(str(len(item_names)))

    for item in removed_item:
        products_page.remove_product_by_name(item)

    expect(products_page.get_cart_count()).to_have_text(str(len(item_names)-len(removed_item)))

    expected_items=item_names.copy()
    
    for item in removed_item:
        expected_items.remove(item)
    

    products_page.open_cart()
    cart_page =CartPage(products_page.page)
    assert cart_page.get_cart_item_names()==expected_items




