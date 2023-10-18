from selenium import webdriver
from selenium.webdriver.common.by import By


class Body:
    sorting_dropdown_xpath: str = "//select[@id = 'products-orderby']"
    selected_sorting4_option_xpath: str = "//select[@id = 'products-orderby']/option[4]"
    selected_sorting2_option_xpath: str = "//select[@id = 'products-orderby']/option[2]"
    pagination_dropdown_xpath: str = "//select[@id = 'products-pagesize']"
    selected_pagination2_option_xpath: str = "//select[@id = 'products-pagesize']/option[2]"
    product_xpath: str = "//a[@title = 'Show details for Blue and green Sneaker']"
    add_to_wishlist_xpath: str = "//input[@id = 'add-to-wishlist-button-28']"
    bar_adding_to_wishlist_xpath: str = "//div[@id = 'bar-notification']/p[@class = 'content']"
    add_to_shoppingcart_xpath: str = "//input[@id = 'add-to-cart-button-28']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_sorting_dropdown(self) -> None:
        self.driver.find_element(By.XPATH, self.sorting_dropdown_xpath).click()

    def select_sorting_option4(self) -> None:
        self.driver.find_element(By.XPATH, self.selected_sorting4_option_xpath).click()

    def get_selected_option4_attribute(self) -> bool:
        return self.driver.find_element(By.XPATH, self.selected_sorting4_option_xpath).get_attribute("selected")

    def select_sorting_option2(self) -> None:
        self.driver.find_element(By.XPATH, self.selected_sorting2_option_xpath).click()

    def get_selected_option2_attribute(self) -> bool:
        return self.driver.find_element(By.XPATH, self.selected_sorting2_option_xpath).get_attribute("selected")

    def click_pagination_dropdown(self) -> None:
        return self.driver.find_element(By.XPATH, self.pagination_dropdown_xpath).click()

    def select_pagination_option2(self) -> None:
        self.driver.find_element(By.XPATH, self.selected_pagination2_option_xpath).click()

    def get_selected_pagination2_attribute(self) -> bool:
        return self.driver.find_element(By.XPATH, self.selected_pagination2_option_xpath).get_attribute("selected")

    def click_product(self) -> None:
        self.driver.find_element(By.XPATH, self.product_xpath).click()

    def add_to_wishlist(self) -> None:
        self.driver.find_element(By.XPATH, self.add_to_wishlist_xpath).click()

    def verify_notification_appearing(self) -> str:
        return self.driver.find_element(By.XPATH, self.bar_adding_to_wishlist_xpath).text

    def add_to_shoppingcart(self) -> None:
        self.driver.find_element(By.XPATH, self.add_to_shoppingcart_xpath).click()
