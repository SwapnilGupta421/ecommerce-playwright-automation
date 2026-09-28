from playwright.sync_api import Page, expect


def test_saucedemo_login(login_page):
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    assert login_page.is_logged_in()

def test_saucedemo_login_incorrect_password(login_page):
    login_page.open()
    login_page.login("standard_user","secret_sauce1")
    
    assert login_page.get_error_message()=="Epic sadface: Username and password do not match any user in this service"

def test_saucedemo_empty_login(login_page):
    login_page.open()
    login_page.login("","")
    
    assert login_page.get_error_message()=="Epic sadface: Username is required"
   