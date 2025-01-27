
class Site:
    def __init__(self, driver):
        self.driver = driver

    def get_protocol(self) -> str:
        return "https"

    def get_domain(self) -> str:
        return "sweetshop.netlify.app"

    def get_address(self) -> str:
        return self.get_protocol() + "://" + self.get_domain()
