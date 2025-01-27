from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.site import Site


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.the_site = Site(self.driver)

    #
    # Page characteristics
    #
    def get_address(self) -> str:
        return self.the_site.get_address()

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return self.driver.find_element(By.XPATH, "//header//h1[text()='Welcome to the sweet shop!']").is_displayed()


    #
    # Page elements
    #


    #
    # Page actions
    #
    def open_page(self):
        self.driver.get(self.get_address())

    def browse_sweets(self):
        self.driver.find_element(By.ID, "submit").click()  # Submit button ID

    def goto_sweets(self):
        self.driver.find_element(By.XPATH, "//*[@id='navbarColor01']//a[text()='Sweets']").click()

    def goto_login(self):
        login_link = self.driver.find_element(By.XPATH, "//*[@id='navbarColor01']//a[text()='Login']")
        login_link.click()
