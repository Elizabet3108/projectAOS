from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Cart_pane:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def table(self):
        """Returns the table element"""
        return self.driver.find_element(By.XPATH, "//li/tool-tip-cart")

    def list_quantity(self):
        """Returns a list with quantity for each product"""
        list_quantity = self.driver.find_elements(By.XPATH, "//*[@id='product']/td/a/label[1]")
        new_list = []
        for i in list_quantity:
            new_list.append(int(i.get_attribute("innerHTML")[5]))
        return new_list

    def list_colors(self):
        """Returns a list with colors"""
        list_color = self.driver.find_elements(By.XPATH, "//*[@id='product']/td/a/label[2]/span")
        new_list = []
        for i in list_color:
            new_list.append(i.get_attribute("innerHTML"))
        return new_list

    def name_products(self):
        """Returns a list with name products"""
        list_name = self.driver.find_elements(By.XPATH, "//*[@id='product']/td/a/h3")
        new_list = []
        for i in list_name:
            new_list.append(i.get_attribute("innerHTML")[:27].rstrip())
        return new_list

    def list_price(self):
        """Returns a list with prices"""
        price = self.driver.find_elements(By.XPATH, "//*/div/table/tbody/tr/td[3]/p")
        new_price = []
        for i in price:
            element = i.get_attribute("innerHTML")[1:].replace(',', '')
            new_price.append(float(element))
        return new_price

    def remove_first_product(self):
        """Click on the cross to remove the first product"""
        rem = self.driver.find_element(By.XPATH, "//*[@class='closeDiv']/*")
        action_chain = ActionChains(self.driver)
        return action_chain.move_to_element(rem).click().perform()