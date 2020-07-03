from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Login_Page import LoginPage


class RepositoryPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def new_repository(self):
        return self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@aria-label='Repositories']//a[contains(@href, 'new')]")))

    def create_repository(self):
        from Pages.New_Repository_Page import NewRepositoryPage
        self.new_repository.click()
        return NewRepositoryPage(self.driver)