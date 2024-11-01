from selenium import webdriver
from selenium.webdriver.common.by import By


#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is ${price_dollar}.${price_cents}")

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

element_found_by_x_path = driver.find_element(By.XPATH, value='//*[@id="python-network"]')
print(element_found_by_x_path.text)

#Close will close a specific tab
# driver.close()

#Quit will close the browser (All tabs)
driver.quit()