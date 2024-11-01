import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10
SPEED_TEST_URL = 'https://www.speedtest.net/'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        accept_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(60)

        close_popup = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')))
        close_popup.click()

        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = down.text

        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = up.text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
