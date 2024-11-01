from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

element_found_by_x_path = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_array_list = element_found_by_x_path.text.split('\n')
my_dict = {round(i / 2): {'time': events_array_list[i], 'name': events_array_list[i + 1]} for i in range(0, len(events_array_list), 2)}
print(my_dict)