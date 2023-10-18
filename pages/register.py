from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random


class Register:
    gender_radiobutton_xpath: str = "//input[@id = 'gender-male']"
    first_name_xpath: str = "//input[@id = 'FirstName']"
    last_name_xpath: str = "//input[@id = 'LastName']"
    email_xpath: str = "//input[@id = 'Email']"
    password_xpath: str = "//input[@id = 'Password']"
    confirm_password_xpath: str = "//input[@id = 'ConfirmPassword']"
    register_button_xpath: str = "//input[@id = 'register-button']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def select_gender(self)-> None:
        self.driver.find_element(By.XPATH, self.gender_radiobutton_xpath).click()

    def enter_first_name(self) -> None:
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys('FirstName')

    def enter_last_name(self) -> None:
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys('LastName')

    def enter_email(self) -> None:
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(self.generate_random_email())



    def enter_password(self) -> None:
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys('Password123!')

    def confirm_password(self) -> None:
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys('Password123!')

    def click_register(self)-> None:
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

    @staticmethod
    def generate_random_email() -> str:
        domain = "test.com"
        username = ''.join(
            random.choices(string.ascii_letters + string.digits, k=10))
        email = f"{username}@{domain}"
        return email




