from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.site import Site


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.the_site = Site(self.driver)

        self.endpoint = "login"

    #
    # Page characteristics
    #
    def get_address(self) -> str:
        return self.the_site.get_address() + "/" + self.endpoint

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return self.page_header().is_displayed()

    #
    # Page elements
    #
    def page_header(self) -> WebElement:
        # used an xpath as there is no unique ID to link to
        return self.driver.find_element(By.XPATH, "//header//h1[text()='Login']")

    def form_field_email(self) -> WebElement:
        return self.driver.find_element(By.ID, "exampleInputEmail")

    def form_field_email_invalid_feedback(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//form//div[contains(text(),'Please enter a valid email address.')]")

    def form_field_password(self) -> WebElement:
        return self.driver.find_element(By.ID, "exampleInputPassword")

    def form_field_password_invalid_feedback(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//form//div[contains(text(),'Please enter a valid password.')]")

    #
    # Page actions
    #
    def open_page(self):
        self.driver.get(self.get_address())
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def enter_email(self, email):
        self.form_field_email().send_keys(
            email
        )

    def enter_password(self, password):
        self.driver.find_element(By.ID, "exampleInputPassword").send_keys(
            password
        )

    def submit_credentials(self):
        # used an xpath as there is no unique ID to link to
        self.driver.find_element(By.XPATH, "//form//button[text()='Login']").click()