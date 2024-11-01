import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Form:

    def __init__(self):
        self.driver = None
        self.form_url = 'https://forms.gle/GWMhXrnRAyQcV2td8'
        self.google_docs_url = 'https://docs.google.com/forms/u/0/'

    def fill_form(self, address: str, price: str, property_link: str):
        self.driver = webdriver.Chrome()
        self.driver.get(self.form_url)
        time.sleep(3)

        address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        price_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        link_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        send_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

        address_input = self.driver.find_element(By.XPATH, address_input_xpath)
        address_input.send_keys(address)

        price_input = self.driver.find_element(By.XPATH, price_input_xpath)
        price_input.send_keys(price)

        link_input = self.driver.find_element(By.XPATH, link_input_xpath)
        link_input.send_keys(property_link)

        send_button = self.driver.find_element(By.XPATH, send_button_xpath)
        send_button.click()

    def send_another_report(self):
        send_another_report = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        send_another_report.click()

    def save_to_spreed_sheet(self):
        form_xpath = '//*[@id=":3b"]/div[1]'
        response_tab_xpath = '//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div'
        spreed_sheet_link_xpath = '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]'
        create_button_xpath = '//*[@id="yDmH0d"]/div[16]/div/div[2]/div[2]/div[3]/div[1]/span/span'

        self.driver.get(self.google_docs_url)
        time.sleep(3)

        form = self.driver.find_element(By.XPATH, form_xpath)
        form.click()

        response_tab = self.driver.find_element(By.XPATH, response_tab_xpath)
        response_tab.click()

        spreed_sheet = self.driver.find_element(By.XPATH, spreed_sheet_link_xpath)
        spreed_sheet.click()

        create_button = self.driver.find_element(By.XPATH, create_button_xpath)
        create_button.click()

        time.sleep(30)
        self.driver.quit()



