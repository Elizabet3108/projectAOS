from unittest import TestCase
from selenium import webdriver
from random import randint, choice
from time import sleep
from examples.projectAOS.Main_page import Main_Page
from examples.projectAOS.Category_page import Category_Page
from examples.projectAOS.Product_page import Product_Page
from examples.projectAOS.Top_panel import Top_Panel
from selenium.webdriver.common.keys import Keys
from examples.projectAOS.Cart_page import Cart_page
from examples.projectAOS.Account import Account
from examples.projectAOS.Order_payment_page import Order_Payment
from examples.projectAOS.Cart_pane import Cart_pane
from examples.projectAOS.Product import Product
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_AOS(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)

        self.main_page = Main_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.top_panel = Top_Panel(self.driver)
        self.cart_page = Cart_page(self.driver)
        self.account = Account(self.driver)
        self.order_payment = Order_Payment(self.driver)
        self.cart_pane = Cart_pane(self.driver)
        self.action_chain = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test1_total_items(self):
        """The test checks if the quantity of the product corresponds to the quantity in the cart"""
        products_name =[]
        for i in range(2):
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2, 9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
            else:
                i -= 1
        list_quantity = self.cart_pane.list_quantity()
        self.assertEqual(str(sum(list_quantity)), self.top_panel.total_items().text)

    def test2_description_products(self):
        """The test checks if the product description matches the description in the shopping cart window"""
        products_name = []
        products_color = []
        products_quantity = []
        price = []
        for i in range(3):
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2,9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
                products_name.append(self.product_page.product_name())
                products_color.append(self.product_page.color())
                products_quantity.append(int(self.product_page.quantity_value()))
                price.append(round(float(self.product_page.product_price()), 2)*quantity)
            else:
                i -= 1
            self.top_panel.logo()
        self.assertEqual(products_name[::-1], self.cart_pane.name_products())
        self.assertEqual(products_color[::-1], self.cart_pane.list_colors())
        self.assertEqual(products_quantity[::-1], self.cart_pane.list_quantity())
        self.assertEqual(price[::-1], self.cart_pane.list_price())

    def test3_remove_product(self):
        """The test checks if after deleting the product, it disappears from the shopping cart window"""
        products_name = []
        for i in range(2):
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2, 9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
            else:
                i -= 1

        list_products = self.cart_pane.name_products()
        self.cart_pane.remove_first_product()
        self.assertNotIn(list_products[0],self.cart_pane.name_products())

    def test4_shopping_cart_page(self):
        """The test checks if the transition to the shopping cart page using the cart icon"""
        list_categories = self.main_page.categories()
        choice(list_categories).click()
        products = self.category_page.products()
        choice(products).click()
        quantity = randint(2, 9)
        self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
        self.product_page.add_to_cart()
        self.top_panel.cart_icon().click()
        self.assertEqual(self.cart_page.shopping_cart_page().text, "SHOPPING CART")

    def test5_match_the_prices(self):
        """The test checks if all prices match the prices in the shopping cart, with the quantity and their amount"""
        products_name = []
        products_quantity = []
        price = []
        price_with_quantity = []
        list_products = []
        for i in range(3):
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2, 9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
                products_name.append(self.product_page.product_name())
                products_quantity.append(int(self.product_page.quantity_value()))
                price.append(round(float(self.product_page.product_price()), 2))
                list_products.append(Product(products_name[i], price[i], products_quantity[i]))
                print(list_products[i])
                price_with_quantity.append(round(float(self.product_page.product_price()) * quantity, 2))
                print(price_with_quantity[i])
            else:
                i -= 1

        self.top_panel.cart_icon().click()
        self.assertEqual(price_with_quantity[::-1], self.cart_page.list_price())
        self.assertEqual(round(sum(price_with_quantity), 2), round(float(self.cart_page.total_price()), 2))

    def test6_changing_quantity(self):
        """The test checks if the number of items changes, as well as changes in the cart"""
        products_name = []
        for i in range(2):
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2,9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
            else:
                i -= 1
            self.top_panel.logo()
        self.top_panel.cart_icon().click()
        self.action_chain.move_to_element(self.cart_page.shopping_cart_page()).perform()
        self.wait.until(EC.invisibility_of_element_located(self.cart_pane.table()))
        edits = self.cart_page.edit()
        for j in range(len(edits)):
            self.cart_page.edit()[j].click()
            self.product_page.quantity().send_keys(Keys.BACKSPACE, str(1))
            self.product_page.add_to_cart()
            self.top_panel.cart_icon().click()
        self.assertEqual(self.cart_page.quantity()[0].text, "1")
        self.assertEqual(self.cart_page.quantity()[1].text, "1")

    def test7_navigate_pages(self):
        """The test checks the transition between the category page and main page"""
        self.main_page.category_tablets()
        products = self.category_page.products()
        choice(products).click()
        self.driver.back()
        self.assertEqual(self.category_page.tablets_page(), "TABLETS")
        self.driver.back()
        sleep(2)
        self.assertEqual(self.main_page.main_page(), "OUR PRODUCTS")

    def test8_SafePay_method(self):
        """The test checks that after creating a new account and paying order with SafePay method,
         the shopping cart empty and the order is on the page 'my orders' """
        for i in range(2):
            products_name = []
            self.top_panel.logo()
            list_categories = self.main_page.categories()
            choice(list_categories).click()
            products = self.category_page.products()
            choice(products).click()
            name = self.product_page.product_name()
            """This is 'if' it is intended so that random does not choose the same product"""
            if name not in products_name:
                quantity = randint(2, 9)
                self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
                self.product_page.add_to_cart()
            else:
                i -= 1
        self.top_panel.cart_icon().click()
        self.cart_page.checkout()
        self.order_payment.registration()
        self.account.new_username("ElizabetMmdv")
        self.account.new_password("12345eM")
        self.account.Email("123@g.com")
        self.account.confirm_password("12345eM")
        self.account.i_agree()
        self.account.button_register().click()
        self.order_payment.next_button()
        self.order_payment.SafePay_username("ElizabetE")
        self.order_payment.SafePay_password("1234Qw")
        self.order_payment.pay_button_SP()
        sleep(2)
        order_number = self.order_payment.order_number()

        self.assertEqual(self.order_payment.order_successfully(), "Thank you for buying with Advantage")

        self.top_panel.cart_icon().click()
        self.assertEqual(self.cart_page.cart_empty(), "Your shopping cart is empty")

        self.top_panel.user_icon()
        self.wait.until(EC.invisibility_of_element_located(self.cart_pane.table()))
        self.top_panel.my_orders()
        self.assertEqual(self.top_panel.order_number(), order_number)

        self.top_panel.user_icon()
        self.wait.until(EC.invisibility_of_element_located(self.cart_pane.table()))
        self.top_panel.my_account()
        self.account.delete_account()
        self.account.button_yes()

    def test9_credit_card_method(self):
        """The test checks that after logging into personal account and paying order with a credit cart,
         the shopping cart empty and the order is on the page 'my orders' """
        list_categories = self.main_page.categories()
        choice(list_categories).click()
        products = self.category_page.products()
        choice(products).click()
        quantity = randint(2, 9)
        self.product_page.quantity().send_keys(Keys.BACKSPACE, str(quantity))
        self.product_page.add_to_cart()
        self.top_panel.cart_icon().click()
        self.cart_page.checkout()
        self.order_payment.username("ElizabetM")
        self.order_payment.password("12345eM")
        self.order_payment.login()
        self.order_payment.next_button()
        self.order_payment.credit_card()
        self.order_payment.card_number("123456781234")
        self.order_payment.cvv_number("123")
        self.order_payment.month("08")
        self.order_payment.year("2025")
        self.order_payment.cardholder_name("ElizabetM")
        self.order_payment.check_mark()
        self.order_payment.pay_button_Card()
        order_number = self.order_payment.order_number()
        self.top_panel.cart_icon().click()
        self.assertEqual(self.cart_page.cart_empty(), "Your shopping cart is empty")
        self.top_panel.user_icon()
        self.wait.until(EC.invisibility_of_element_located(self.cart_pane.table()))
        self.top_panel.my_orders()
        self.assertEqual(self.top_panel.order_number(), order_number)

    def test10_sign_out_in(self):
        """The test checks if you are logging in and out of your personal account"""
        self.top_panel.user_icon()
        self.account.username("ElizabetM")
        self.account.password("12345eM")
        self.account.sign_in()
        sleep(2)
        self.assertEqual(self.account.account_page().text, "ElizabetM")

        self.top_panel.user_icon()
        self.account.sign_out()
        sleep(2)
        self.assertFalse(self.account.account_page().text, "ElizabetM")

    def tearDown(self):
        self.top_panel.logo()
        self.driver.quit()





