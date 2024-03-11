from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def shopping_cart_page(self):
        """Returns the shopping cart element"""
        return self.driver.find_element(By.XPATH, "//*[@class='uiview ng-scope']/section/article/nav/a[2]")

    def quantity(self):
        """Returns a list with the quantity of each product"""
        return self.driver.find_elements(By.XPATH, "//*[@id='shoppingCart']/table/tbody/tr/td[5]")

    def checkout(self):
        """Click on the checkout button"""
        self.driver.find_element(By.XPATH, "//*[@id='shoppingCart']/table/tfoot/tr[2]/td/button").click()

    def list_price(self):
        """Returns a list with the price of each product"""
        price = self.driver.find_elements(By.XPATH, "//*[@id='shoppingCart']/table/tbody/tr/td[6]/p")
        new_price = []
        for i in price:
            element = i.get_attribute("innerHTML").replace(',', '').replace('$', '')
            new_price.append(round(float(element), 2))
        return new_price

    def total_price(self):
        """Returns the total price element"""
        price = self.driver.find_element(By.XPATH, "//*[@id='shoppingCart']/table/tfoot/tr/td[2]/span[2]").text[1:]
        return price.replace(',', '')

    def edit(self):
        """Returns a list with edit button for each product"""
        return self.driver.find_elements(By.XPATH, "//*[@id='shoppingCart']/table/tbody/tr/td[6]/span/a[1]")

    def cart_empty(self):
        """Returns the title cart empty element"""
        return self.driver.find_element(By.XPATH, "//*[@id='shoppingCart']/div/label").text