from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    remove_checkbox_xpath: str = "//td[@class = 'remove-from-cart']/input[@type = 'checkbox']"
    update_cart_xpath: str = "//input[@name = 'updatecart']"
    text_in_shoppingcart_xpath: str = "//div[@class = 'order-summary-content']"
    country_dropdown_xpath: str = "//select[@id = 'CountryId']"
    selected_country_xpath: str = "//select[@id = 'CountryId']/option[@value = '12']"
    select_agree_checkbox_xpath: str = "//div[@class = 'terms-of-service']/input[@id = 'termsofservice']"
    checkout_button_xpath: str = "//button[@id = 'checkout']"
    address_country_dropdown_xpath: str = "//select[@id = 'BillingNewAddress_CountryId']"
    address_country_xpath: str = "//select[@id = 'BillingNewAddress_CountryId']/option[@value = '28']"
    address_city_xpath: str = "//input[@id = 'BillingNewAddress_City']"
    address_address1_xpath: str = "//input[@id = 'BillingNewAddress_Address1']"
    address_zip_xpath: str = "//input[@id = 'BillingNewAddress_ZipPostalCode']"
    address_phone_xpath: str = "//input[@id = 'BillingNewAddress_PhoneNumber']"
    continue_oncheckout_button_xpath: str = "//input[@class = 'button-1 new-address-next-step-button']"
    continue_shipping_button_xpath: str = "//input[@class = 'button-1 shipping-method-next-step-button']"
    continue_payment_button_xpath: str = "//input[@class = 'button-1 payment-method-next-step-button']"
    confirm_checkout_button_xpath: str = "//input[@class = 'button-1 confirm-order-next-step-button']"
    existed_address_dropdown_xpath: str = "//select[@id = 'billing-address-select']"
    new_address_option_xpath: str = "//select[@id = 'billing-address-select']/option[@value = '']"
    continue_payment_info_button_xpath: str = "//input[@class = 'button-1 payment-info-next-step-button']"
    shipping_method_xpath: str = "//div[@class = 'method-name']/input[@id = 'shippingoption_1']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_address_country_dropdown(self) -> None:
        self.driver.find_element(By.XPATH, self.address_country_dropdown_xpath).click()

    def select_shipping_method_radiobutton(self) -> None:
        self.driver.find_element(By.XPATH, self.shipping_method_xpath).click()



    def click_existed_address_dropdown(self) -> None:
        self.driver.find_element(By.XPATH, self.existed_address_dropdown_xpath).click()

    def select_newaddress_for_checkout(self) -> None:
        self.driver.find_element(By.XPATH, self.new_address_option_xpath).click()

    def select_agree_checkbox(self) -> None:
        self.driver.find_element(By.XPATH, self.select_agree_checkbox_xpath).click()

    def select_address_country(self) -> None:
        self.driver.find_element(By.XPATH, self.address_country_xpath).click()

    def enter_address_city(self) -> None:
        self.driver.find_element(By.XPATH, self.address_city_xpath).send_keys('City')

    def enter_address1(self) -> None:
        self.driver.find_element(By.XPATH, self.address_address1_xpath).send_keys('Some address 28')

    def enter_address_zip(self) -> None:
        self.driver.find_element(By.XPATH, self.address_zip_xpath).send_keys('123456')

    def enter_address_phonenumber(self) -> None:
        self.driver.find_element(By.XPATH, self.address_phone_xpath).send_keys('123456')

    def click_address_continue_button(self) -> None:
        self.driver.find_element(By.XPATH, self.continue_oncheckout_button_xpath).click()

    def click_shipping_continue_button(self) -> None:
        self.driver.find_element(By.XPATH, self.continue_shipping_button_xpath).click()

    def click_payment_continue_button(self) -> None:
        self.driver.find_element(By.XPATH, self.continue_shipping_button_xpath).click()


    def click_payment_info_continue_button(self) -> None:
        self.driver.find_element(By.XPATH, self.continue_payment_info_button_xpath).click()

    def click_confirm_button(self) -> None:
        self.driver.find_element(By.XPATH, self.confirm_checkout_button_xpath).click()

    def select_checkbox(self) -> None:
        self.driver.find_element(By.XPATH, self.remove_checkbox_xpath).click()

    def remove_product(self) -> None:
        self.driver.find_element(By.XPATH, self.update_cart_xpath).click()

    def get_text_from_shoppingcart(self) -> str:
        return self.driver.find_element(By.XPATH, self.text_in_shoppingcart_xpath).text

    def click_countrydropdown_for_checkout(self) -> None:
        self.driver.find_element(By.XPATH, self.country_dropdown_xpath).click()

    def select_country_for_checkout(self) -> None:
        self.driver.find_element(By.XPATH, self.selected_country_xpath).click()

    def click_checkout_button(self) -> None:
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()
