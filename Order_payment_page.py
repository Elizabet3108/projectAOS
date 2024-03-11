from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Order_Payment:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def registration(self):
        """Click on the register button"""
        self.driver.find_element(By.ID, "registration_btn").click()

    def username(self, username):
        """Key for username in order payment page"""
        self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)

    def password(self, password):
        """Key for password in order payment page"""
        self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def login(self):
        """Click on the login button"""
        self.driver.find_element(By.ID, "login_btn").click()

    def next_button(self):
        """Click on the next button"""
        self.driver.find_element(By.XPATH, "//*[@class='mobileBtnHandler']/button").click()

    def credit_card(self):
        """Click on the credit cart method"""
        self.driver.find_element(By.XPATH, "//*[@class='paymentMethods']/div[2]").click()
        # self.driver.find_element(By.CSS_SELECTOR, "[id='creditCard']")

    def card_number(self, num):
        """Key for card number"""
        self.driver.find_element(By.CSS_SELECTOR, "[id='creditCard']").send_keys(num)

    def cvv_number(self, num):
        """Key for cvv number"""
        self.driver.find_element(By.CSS_SELECTOR, "[name='cvv_number']").send_keys(num)

    def cardholder_name(self, name):
        """Key for cardholder name"""
        self.driver.find_element(By.CSS_SELECTOR, "[name='cardholder_name']").send_keys(name)

    def month(self, num):
        """Month in credit card method for pay order"""
        month = self.driver.find_element(By.CSS_SELECTOR, "[name='mmListbox']")
        dropdown = Select(month)
        dropdown.select_by_visible_text(num)

    def year(self, num):
        """Year in credit card method for pay order"""
        year = self.driver.find_element(By.CSS_SELECTOR, "[name='yyyyListbox']")
        dropdown = Select(year)
        dropdown.select_by_visible_text(num)

    def check_mark(self):
        """Click on the check mark to remove it"""
        self.driver.find_element(By.CSS_SELECTOR, "[name='save_master_credit']").click()

    def pay_button_Card(self):
        """Click on the pay button for credit card"""
        self.driver.find_element(By.ID, "pay_now_btn_ManualPayment").click()

    def SafePay_username(self, username):
        """Key for username for SafePay"""
        self.driver.find_element(By.NAME, "safepay_username").send_keys(username)

    def SafePay_password(self, password):
        """Key for password for SafePay"""
        self.driver.find_element(By.XPATH, "//*[@id='paymentMethod']/div/div[2]/sec-form/sec-view[2]/div/input").send_keys(password)

    def pay_button_SP(self):
        """Click on the pay button for SafePay"""
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def order_successfully(self):
        """Returns the title for order successfully"""
        return self.driver.find_element(By.XPATH, "//*[@id='orderPaymentSuccess']/h2/span").text

    def order_number(self):
        """Returns the order number"""
        return self.driver.find_element(By.XPATH, "//*[@id='orderPaymentSuccess']/p/label[2]").text

