import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://github.com/login')
wait = WebDriverWait(driver, 10)

log = 'crazydrone69'
passw = 'Fuhtcjh1984'

# login page
login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_field"))).send_keys(log)
password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(passw)
signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'commit']"))).click()

# time.sleep(3)

# home page
profile_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "summary[aria-label*='profile and more']"))).click()
profile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-hydro-click*='YOUR_PROFILE']"))).click()

time.sleep(3)

# By.cssSelector("div[class='ajax_enabled'] [style='display:block']"));
# ("div:contains('_pattern_')"));

# profile
repositories = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-hydro-click*='TAB_REPOSITORIES']"))).click()
new_repository = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@aria-label='Repositories']//a[contains(@href, 'new')]"))).click()
# time.sleep(5)

# new_repository
repo_name = "bla-bla8"
repository_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#repository_name"))).send_keys(repo_name)
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create repository')]"))).click()
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.XPATH, f"//h1/strong//a[contains(text(), {repo_name})]"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(data-selected-links, '{log}/{repo_name}/settings'"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//summary[contains(text(), 'Delete this repository')]"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH,
                                             "//input[@aria-label='Type in the name of the repository to confirm that you want to delete this repository.']"))).send_keys(f'{log}/{repo_name}')
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'I understand the consequences, delete this repository')]"))).click()

time.sleep(5)



