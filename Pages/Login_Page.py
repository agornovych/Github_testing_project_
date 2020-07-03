from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Home_Page import HomePage


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def login_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_field")))

    @property
    def password_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))

    @property
    def signin_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'commit']")))

    # @property
    # def error_message(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Incorrect username or password.')]")))

    def enter_email(self, login):
        self.login_field.send_keys(login)
        return self

    def enter_password(self, password):
        self.password_field.send_keys(password)
        return self

    def get_signin(self):
        self.signin_button.click()
        return HomePage(self.driver)

    # def get_error_message(self):
    #     return self.driver.title
            # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Incorrect username or password.')]"))).text()

