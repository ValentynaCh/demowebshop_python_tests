from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Header:
    login_button_xpath: str = "//a[@href = '/login']"
    register_button_xpath: str = "//a[@href = '/register']"
    account_email_xpath: str = "//a[@class = 'account']"
    menu_item_xpath: str = "//ul[@class='top-menu']//a[@href='/{}']"
    sub_menu_items_xpath: str = menu_item_xpath + "/ancestor::li/ul//a"
    shopping_cart_xpath: str = "//a[@class = 'ico-cart']/span[@class = 'cart-label']"





    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_login(self)-> None:
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_register(self)-> None:
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

    def get_account_email(self):
        return self.driver.find_element(By.XPATH, self.account_email_xpath).text

    def get_submenu_items_from_parent_name(self, menu_name: str = 'computers') -> list:
        print(f"Get links from [{menu_name}] menu")
        chain = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.menu_item_xpath.format(menu_name))
        chain.move_to_element(element).perform()
        return [item.text for item in self.driver.find_elements(By.XPATH, self.sub_menu_items_xpath.format(menu_name))]

    def click_shopping_bag(self) -> None:
        self.driver.find_element(By.XPATH, self.shopping_cart_xpath).click()







