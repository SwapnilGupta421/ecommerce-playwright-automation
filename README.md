# E-commerce Playwright Automation

E-commerce UI automation framework built using **Python, Playwright, and Pytest** for testing the [SauceDemo](https://www.saucedemo.com/) application.

## Tech Stack

* **Python 3**
* **Playwright**
* **Pytest**
* **Pytest-Playwright**
* **Pytest-HTML**
* **Page Object Model (POM)**



## Project Structure

ecommerce-playwright-automation/
|
+-- api/
|   +-- api_client.py
|   +-- api_config.py
|   +-- api_assertions.py
|   +-- test_data.py
|   +-- test_api.py
|
+-- pages/
|   +-- login_page.py
|   +-- product_page.py
|   +-- cart_page.py
|   +-- checkout_page.py
|
+-- tests/
|   +-- test_login.py
|   +-- test_products.py
|   +-- test_cart.py
|   +-- test_checkout.py
|
+-- .github/
|   +-- workflows/
|       +-- playwright-tests.yml
|
+-- conftest.py
+-- pytest.ini
+-- requirements.txt
+-- README.md

## Automated Test Coverage

### Login

* Valid login
* Invalid username/password
* Empty username
* Empty password

### Products

* Add a single product
* Add multiple products
* Add all products
* Validate product names

### Cart

* Validate cart item count
* Validate cart badge count
* Remove product by name
* Validate product prices
* Validate cart quantities

### Checkout

* Enter customer information
* Validate Checkout Overview page
* Validate item total
* Validate tax
* Validate final total
* Complete checkout
* Validate order confirmation
* Return to Products page

## Framework Features

* Page Object Model for maintainable test automation
* Pytest fixtures for reusable setup
* Parameterized tests for multiple test scenarios
* Custom Pytest markers for Smoke and Regression tests
* Automatic screenshots when tests fail
* HTML test reports
* Playwright auto-waiting and assertions
* Reusable page methods and locators

## Installation

Clone the repository:



git clone https://github.com/SwapnilGupta421/ecommerce-playwright-automation.git
cd ecommerce-playwright-automation



Create and activate a virtual environment:



python -m venv .venv



Windows:

powershell
.venv\\Scripts\\Activate.ps1



Install dependencies:



pip install -r requirements.txt



Install Playwright browsers:



playwright install



## Running Tests

Run all tests:



pytest



Run tests with browser visible:



pytest --headed



Run with slow motion for demonstration:



pytest --headed --slowmo 900



Run Smoke tests:



pytest -m smoke



Run Regression tests:



pytest -m regression



## HTML Test Report

Generate an HTML report:



pytest --html=reports/report.html --self-contained-html



The report will be generated under:

text
reports/report.html



## Failure Screenshots

The framework automatically captures a screenshot when a test fails.

Screenshots are saved under:

text
screenshots/



## Purpose

This project demonstrates practical UI test automation using **Python, Playwright, Pytest, Page Object Model, test parametrization, synchronization, assertions, reporting, and failure diagnostics**.





## API Automation



API automation is implemented using Python, Pytest, and Requests with a reusable API client and assertion utilities.



###### API Coverage

* GET all users
* GET user by ID
* POST create user
* PUT update user
* DELETE user
* Negative testing for non-existing users
* Parametrized API tests
* Response status and header validation
* Response field validation
* Environment-based API configuration



###### API Framework Structure

api/
|
+-- api_client.py
+-- api_config.py
+-- api_assertions.py
+-- test_data.py
+-- test_api.py


Run all tests:
pytest


Run only API tests:
pytest api/test_api.py


Run API tests with detailed output:
pytest api/test_api.py -v -s

## Continuous Integration

The project uses **GitHub Actions** to automatically run the UI and API test suite.

The workflow is triggered when:

- Code is pushed to the `main` branch
- A pull request is created against the `main` branch

The CI workflow:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Installs Playwright browsers
5. Runs the complete Pytest test suite

This helps verify that the automation framework works in a clean CI environment.

