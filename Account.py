from selenium import webdriver
from selenium.webdriver.common.by import By

class Account:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def new_username(self, username):
        """Key for username in create account page"""
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(username)

    def new_password(self, password):
        """Key for password in create account page"""
        self.driver.find_element(By.XPATH, "//*[@id='formCover']/div[1]/div[2]/sec-view[1]/div/input").send_keys(password)

    def Email(self, email):
        """Key for email in create account page"""
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(email)

    def confirm_password(self, password):
        """Key for confirm password in create account page"""
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(password)

    def i_agree(self):
        """Element agree and click on that in create account page"""
        self.driver.find_element(By.XPATH, "//*[@id='form']/div/sec-view/div/input").click()

    def button_register(self):
        """Returns the button register element"""
        return self.driver.find_element(By.XPATH, "//*[@class='center']/sec-sender/button")

    def username(self, username):
        """Key for username in the account login window"""
        self.driver.find_element(By.XPATH, "//*[@class='inputContainer ng-scope']/input[@name='username']").send_keys(username)

    def password(self, password):
        """Key for password in the account login window"""
        self.driver.find_element(By.XPATH, "//*[@class='inputContainer ng-scope']/input[@name='password']").send_keys(password)

    def sign_in(self):
        """Click on button 'sign in' in the account login window"""
        self.driver.find_element(By.ID, "sign_in_btn").click()

    def account_page(self):
        """Returns the account name element on top panel"""
        return self.driver.find_element(By.XPATH, "//a[@id='menuUserLink']/span")

    def sign_out(self):
        """Click on button 'sign out' in the window under the user icon"""
        self.driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']/label[3]").click()

    def delete_account(self):
        """Click on 'delete account' """
        self.driver.find_element(By.XPATH, "//*[@class='popup']/div/div[6]/button/div").click()

    def button_yes(self):
        """Click on 'yes' for delete account"""
        self.driver.find_element(By.XPATH, "//*[@id='deleteAccountPopup']/div[3]/div[1]").click()
