from selenium import webdriver
from selenium.webdriver.common.by import By

class Main_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def categories(self):
        """Returns a list with categories"""
        return self.driver.find_elements(By.CLASS_NAME, "shop_now_slider")

    def category_tablets(self):
        """Click on the category tablets element"""
        self.driver.find_element(By.ID, "tabletsTxt").click()

    def main_page(self):
        """Returns the title 'our products' """
        return self.driver.find_element(By.XPATH, "//ul[@class='roboto-light desktop-handler']/li[8]/a").text