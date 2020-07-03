import time
import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login_Page import LoginPage


@pytest.fixture
def login():
    return 'crazydrone69'


@pytest.fixture
def password():
    return 'Fuhtcjh1984'


@pytest.fixture
def login_page(request):
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://github.com/login')

    login_page = LoginPage(driver)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return login_page


def test_signup_positive(login_page, login, password):
    login_page.enter_email(login)
    login_page.enter_password(password)
    login_page.get_signin()


def test_signup_negative(login_page, login, password):
    login_page.enter_email(login+'negative')
    login_page.enter_password(password)
    login_page.get_signin()


def test_filter(login_page, login, password):
    home_page = login_page.enter_email(login).enter_password(password).get_signin()
    home_page.use_filter('test')
    time.sleep(100)
