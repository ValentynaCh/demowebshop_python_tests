from selenium import webdriver
from selenium.webdriver.common.by import By


class Header:
    login_button_xpath: str = "//a[@href = '/login']"
    register_button_xpath: str = "//a[@href = '/register']"
    account_email_xpath: str = "//a[@class = 'account']"
    computers_group_xpath: str = "//ul[@class = 'top-menu']//a[@href = '/computers']/ancestor::li/ul/li/a"
    shopping_cart_xpath: str = "//a[@class = 'ico-cart']/span[@class = 'cart-label']"





    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_login(self)-> None:
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_register(self)-> None:
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

    def get_account_email(self):
        return self.driver.find_element(By.XPATH, self.account_email_xpath).text

    def get_computers_subgroups(self):
        elements = self.driver.find_elements(By.XPATH, self.computers_group_xpath)
        print([element.text for element in elements])
        return [element.text for element in elements]

    def click_shopping_bag(self) -> None:
        self.driver.find_element(By.XPATH, self.shopping_cart_xpath).click()







