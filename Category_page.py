from selenium import webdriver
from selenium.webdriver.common.by import By

class Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def products(self):
        """Returns a list with product names"""
        return self.driver.find_elements(By.XPATH, "//div[@class = 'cell categoryRight']/ul/li/div[@class = 'AddToCard']")

    def tablets_page(self):
        """Returns the title of tablets page element"""
        return self.driver.find_element(By.XPATH, "//nav[@class='pages categoryDataFixedNav']/a[2]").text
