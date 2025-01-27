import pytest
from selenium.common import TimeoutException, ElementNotVisibleException, NoSuchElementException

from tests.pages.account_page import AccountPage
from tests.pages.home_page import HomePage
from tests.pages.login_page import LoginPage

# The website currently has terrible acceptance criteria for a valid email address
valid_credentials = [
    ("Mitchell.Olson41@gmail.com", "Password"),
    ("Doug_Beer68@gmail.com", "Password"),
    ("Adolf.Russel@gmail.com", "Password"),
    ("Myrtie_Rowe35@gmail.com", "Password"),
]

# The website currently allows email addresses that do not conform to actual email format
invalid_emails = [
    ("Mitchell.Olson41@"),
    ("Doug_Beer68"),
    ("@gmail.com"),
    ("gmail.com"),
]

# This website has no acceptance criteria for what a valid password format is - so just using no password
invalid_passwords = [
    (""),
]


def test_access_login_page_from_home_page(driver):
    driver.maximize_window()
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Given the user is on the home page
    home_page.open_page()

    # When the user goes to Login
    home_page.goto_login()

    # Then the login page is displayed
    try:
        assert login_page.is_displayed()
    except TimeoutException:
        pytest.fail("Login Page Header did not become visible in time")
    except NoSuchElementException:
        pytest.fail("Login Page Header was not found")
    except ElementNotVisibleException:
        pytest.fail("Login Page Header element was not visible")


@pytest.mark.parametrize("email,password", valid_credentials)
def test_valid_credentials_login(driver, email, password):
    driver.maximize_window()
    login_page = LoginPage(driver)
    account_page = AccountPage(driver)

    # Given the user is on the login page
    login_page.open_page()

    # When the user enters correct credentials
    login_page.enter_email(email)
    login_page.enter_password(password)

    # And the user submits their credentials
    login_page.submit_credentials()

    # Then the user will be logged in
    try:
        assert account_page.is_displayed()
    except TimeoutException:
        pytest.fail("Account Page Header did not become visible in time")
    except NoSuchElementException:
        pytest.fail("Account Page Header was not found")
    except ElementNotVisibleException:
        pytest.fail("Account Page Header element was not visible")


@pytest.mark.parametrize("email", invalid_emails)
def test_invalid_email_login(driver, email):
    driver.maximize_window()
    login_page = LoginPage(driver)

    # Given the user is on the login page
    login_page.open_page()

    # When the user enters incorrect credentials
    login_page.enter_email(email)
    login_page.enter_password('Password')

    # And the user submits their credentials
    login_page.submit_credentials()

    # Then the user will get invalid email feedback
    try:
        assert login_page.form_field_email_invalid_feedback().is_displayed()
    except TimeoutException:
        pytest.fail("Invalid email feedback element did not become visible in time")
    except NoSuchElementException:
        pytest.fail("Invalid email feedback element was not found")
    except ElementNotVisibleException:
        pytest.fail("Invalid email feedback element was not visible")


@pytest.mark.parametrize("password", invalid_passwords)
def test_invalid_password_login(driver, password):
    driver.maximize_window()
    login_page = LoginPage(driver)

    # Given the user is on the login page
    login_page.open_page()

    # When the user enters incorrect credentials
    login_page.enter_email('Mitchell.Olson41@gmail.com')
    login_page.enter_password(password)

    # And the user submits their credentials
    login_page.submit_credentials()

    # Then the user will get invalid password feedback
    try:
        assert login_page.form_field_password_invalid_feedback().is_displayed()
    except TimeoutException:
        pytest.fail("Invalid password feedback element did not become visible in time")
    except NoSuchElementException:
        pytest.fail("Invalid password feedback element was not found")
    except ElementNotVisibleException:
        pytest.fail("Invalid password feedback element was not visible")
