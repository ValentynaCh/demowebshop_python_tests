from selenium import webdriver
from selenium.webdriver.common.by import By



class Login:
    gender_radiobutton_xpath: str = "//input[@id = 'gender-male']"
    email_login_xpath: str = "//input[@id = 'Email']"
    password_xpath: str = "//input[@id = 'Password']"
    login_button_xpath: str = "//div[@class = 'buttons'] //input[@type = 'submit']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def enter_login_email(self, email) -> None:
        self.driver.find_element(By.XPATH, self.email_login_xpath).send_keys(email)

    def enter_login_password(self) -> None:
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys('Password123!')

    def click_login(self) -> None:
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
