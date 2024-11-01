from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, 'fName')
first_name_input.send_keys("Leandro")

last_name_input = driver.find_element(By.NAME, 'lName')
last_name_input.send_keys("Palermo")

email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys("leandro@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()



