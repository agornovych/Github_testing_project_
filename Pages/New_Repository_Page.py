from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Login_Page import LoginPage


class NewRepositoryPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def repository_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#repository_name")))

    @property
    def submit_button(self):
        return self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create repository')]")))

    def set_repository_name(self, name):
        self.repository_name.send_keys(name)
        return self

    def create_repository(self):
        self.submit_button.click()
        return self
