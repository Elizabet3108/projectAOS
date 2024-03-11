from selenium import webdriver
from selenium.webdriver.common.by import By

class Top_Panel:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def logo(self):
        """Click on the logo"""
        self.driver.find_element(By.CLASS_NAME, "logo").click()

    def total_items(self):
        """Return total items element"""
        return self.driver.find_element(By.XPATH, "//*[@class='roboto-light desktop-handler']/li[2]/a/span")

    def cart_icon(self):
        """Return the cart icon element"""
        return self.driver.find_element(By.ID, "menuCart")

    def user_icon(self):
        """Click on the user icon"""
        self.driver.find_element(By.ID, "menuUserLink").click()

    def my_orders(self):
        """Click on my orders under the user icon"""
        self.driver.find_element(By.XPATH, "//*[@id='menuUserLink']/div/label[2]").click()

    def my_account(self):
        """Click on my account under the user icon"""
        self.driver.find_element(By.XPATH, "//*[@id='menuUserLink']/div/label[1]").click()

    def order_number(self):
        """Order number in my orders page"""
        return self.driver.find_element(By.XPATH, "//*[@class='orderDetails']/div[1]/label").text


