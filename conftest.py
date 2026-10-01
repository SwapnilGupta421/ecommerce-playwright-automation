import pytest
from pathlib import Path
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screenshot_path = (
                screenshot_dir / f"{item.name}.png"
            )

            page.screenshot(path=str(screenshot_path))
            print(f"\nScreenshot saved: {screenshot_path}")