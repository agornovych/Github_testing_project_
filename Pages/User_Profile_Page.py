from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Login_Page import LoginPage


class UserProfilePage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def repositories(self):
        return self.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-hydro-click*='TAB_REPOSITORIES']")))

    def open_repositories(self):
        from Pages.Repository_Page import RepositoryPage
        self.repositories.click()
        return RepositoryPage(self.driver)

