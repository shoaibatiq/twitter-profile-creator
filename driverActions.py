from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
from time import sleep

class DriverActions():
    def __init__(self, driver):
        self.driver = driver
    @staticmethod
    def random_wait(low, high):
        time_wait = random.uniform(low, high)
        sleep(time_wait)
    def click(self, xpath):
        element = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.random_wait(0.4, 0.7)
        element.click()
    def human_typer(self, xpath, text: str):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        # element.clear()
        for s in text:
            element.send_keys(s)
            sleep(random.uniform(0.07, 0.5))
    def js_click(self, xpath):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].click();", element)
