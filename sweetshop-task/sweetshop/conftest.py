import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


# pytest_plugins = ["pytest_html"]  # Manually register the pytest-html plugin


@pytest.fixture(scope='function')
def driver(request):
    selenium_hub_url = os.getenv("SELENIUM_REMOTE_URL")

    # Get the browser from pytest CLI options (default to Chrome)
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument('--headless')
    elif browser == "edge":
        options = EdgeOptions()
        # options.add_argument('--headless')
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Connect to Selenium Grid using the options
    driver = webdriver.Remote(
        command_executor=selenium_hub_url,
        options=options
    )

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use for tests: chrome or edge"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = (os.path.join(screenshots_dir, f"{item.name}.png"))

            driver.save_screenshot("reports/"+screenshot_path)

            if hasattr(report, "extras"):
                from pytest_html.extras import image  # Import dynamically
                report.extras = getattr(report, "extras", [])
                report.extras.append(image(screenshot_path))
