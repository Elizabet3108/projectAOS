from selenium import webdriver
from selenium.webdriver.common.by import By

class Product_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def quantity(self):
        """Returns the quantity element"""
        return self.driver.find_element(By.XPATH, "//div[@class='e-sec-plus-minus']/div/input")

    def quantity_value(self):
        """Returns the value of quantity"""
        return self.driver.find_element(By.XPATH, "//div[@class='e-sec-plus-minus']/div/input").get_attribute("value")

    def add_to_cart(self):
        """Click on the add to cart"""
        self.driver.find_element(By.XPATH, "//div[@class='fixedBtn']/button").click()

    def product_name(self):
        """Returns the product name"""
        product = self.driver.find_element(By.XPATH, "//*[@class='half'][2]/h1")
        return product.get_attribute("innerHTML")[1:28].rstrip()

    def color(self):
        """Returns the product color"""
        color = self.driver.find_element(By.CLASS_NAME, "colorSelected")
        return color.get_attribute("title")

    def product_price(self):
        """Returns the product price"""
        element = self.driver.find_element(By.XPATH, "//div[@class='half'][2]/h2").text[1:]
        return element.replace(',', '')