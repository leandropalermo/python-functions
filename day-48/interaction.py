from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# element_found = driver.find_element(By.ID, value='articlecount')
# print(element_found.text.split(" ")[0])
#
# element_found_by_css_selector = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(element_found_by_css_selector.text)

# element_found_by_link_text = driver.find_element(By.LINK_TEXT, value="Content portals")
# element_found_by_link_text.click()

element_found_by_input_name = driver.find_element(By.NAME, value="search")
element_found_by_input_name.send_keys("Python", Keys.ENTER)
