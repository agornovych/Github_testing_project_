from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Login_Page import LoginPage


class HomePage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def login_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "summary .Header-link")))

    @property
    def your_profile(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Your profile')]")))

    @property
    def filter(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input #dashboard-repos-filter-left")))

    def open_profile(self):
        self.login_field.click()
        self.your_profile.click()
        return self

    def use_filter(self, text):
        self.filter.send_keys(text)
        return self
