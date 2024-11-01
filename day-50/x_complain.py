from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

x_url = 'https://twitter.com/'
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = ''
USERNAME_X = 'leandro.lpalermo@gmail.com'
PASSWORD_X = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(x_url)

enter_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]')))
# enter_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
# enter_button = driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo > div > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a > div')
enter_button.click()


username_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]')))
username_input.send_keys(USERNAME_X, Keys.ENTER)
# username_input = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
password_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="current-password"]')))
password_input.send_keys(PASSWORD_X, Keys.ENTER)
print(username_input.text)