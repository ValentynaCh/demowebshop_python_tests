import unittest

from selenium import webdriver

from core.driver_manager import Drivers
from enums.browsers import Browsers
from pages.header import Header
from pages.register import Register
from pages.login import Login
from pages.body import Body
from pages.cart import Cart


class TaskTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver: webdriver = Drivers.get_driver(Browsers.firefox)

    def test_user_register(self) -> None:
        page: Header = Header(self.driver)
        page.click_register()

        page_register: Register = Register(self.driver)
        page_register.select_gender()
        page_register.enter_first_name()
        page_register.enter_last_name()
        page_register.enter_email()
        page_register.enter_password()
        page_register.confirm_password()
        page_register.click_register()
        expected_url: str = "https://demowebshop.tricentis.com/registerresult/1"
        self.assertIn(expected_url, self.driver.current_url)

    def test_user_login(self) -> None:
        page: Header = Header(self.driver)
        page.click_login()

        page_login: Login = Login(self.driver)
        page_login.enter_login_email('some_email@gmail.com')
        page_login.enter_login_password()
        page_login.click_login()

        page: Header = Header(self.driver)
        self.assertEquals(page.get_account_email(), 'some_email@gmail.com', 'User has not been logged in')

   #Task 3 is not completed, can not find xpath
    def test_computers_sub_groups(self) -> None:
        page: Header = Header(self.driver)
        page.get_computers_subgroups()
        #plus function to check whether gotten lost is the same as computers enum

    def test_sorting_items(self) -> None:
        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_apparel_shoes: Body = Body(self.driver)
        page_apparel_shoes.click_sorting_dropdown()
        page_apparel_shoes.select_sorting_option2()
        assert page_apparel_shoes.get_selected_option2_attribute()
        print("Soring option 2 is selected")
        page_apparel_shoes.select_sorting_option4()
        assert page_apparel_shoes.get_selected_option4_attribute()
        print("Soring option 4 is selected")

    def test_pagination(self) -> None:
        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_apparel_shoes: Body = Body(self.driver)
        page_apparel_shoes.click_pagination_dropdown()
        page_apparel_shoes.select_pagination_option2()
        assert page_apparel_shoes.get_selected_pagination2_attribute()
        print("Pagination option is selected")

    def test_adding_to_wishlist(self):
        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_body: Body = Body(self.driver)
        page_body.click_product()
        page_body.add_to_wishlist()
        self.assertIn(page_body.verify_notification_appearing(), 'The product has been added to your wishlist')
        print('The product has been added to your wishlist')

    def test_adding_to_shoppingcart(self):
        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_body: Body = Body(self.driver)
        page_body.click_product()
        page_body.add_to_shoppingcart()
        self.assertIn(page_body.verify_notification_appearing(), 'The product has been added to your shopping cart')
        print('The product has been added to your shopping cart')

    def test_removing_product(self):
        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_body: Body = Body(self.driver)
        page_body.click_product()
        page_body.add_to_shoppingcart()

        page: Header = Header(self.driver)
        page.click_shopping_bag()

        page_cart: Cart = Cart(self.driver)
        page_cart.select_checkbox()
        page_cart.remove_product()
        self.assertIn(page_cart.get_text_from_shoppingcart(), 'Your Shopping Cart is empty! ')
        print('The product has been removed')

    def test_checkout_button(self):
        page: Header = Header(self.driver)
        page.click_login()

        page_login: Login = Login(self.driver)
        page_login.enter_login_email('some_email@gmail.com')
        page_login.enter_login_password()
        page_login.click_login()

        self.driver.get('https://demowebshop.tricentis.com/apparel-shoes')
        page_body: Body = Body(self.driver)
        page_body.click_product()
        page_body.add_to_shoppingcart()

        page: Header = Header(self.driver)
        page.click_shopping_bag()

        page_cart: Cart = Cart(self.driver)
        page_cart.click_countrydropdown_for_checkout()
        page_cart.select_country_for_checkout()
        page_cart.select_agree_checkbox()
        page_cart.click_checkout_button()
        page_cart.click_existed_address_dropdown()
        page_cart.select_newaddress_for_checkout()
        page_cart.click_address_country_dropdown()
        page_cart.select_address_country()
        page_cart.enter_address_city()
        page_cart.enter_address1()
        page_cart.enter_address_zip()
        page_cart.enter_address_phonenumber()
        page_cart.click_address_continue_button()
        page_cart.click_address_continue_button()
        #page_cart.select_shipping_method_radiobutton()


        page_cart.click_shipping_continue_button()
        page_cart.click_payment_continue_button()
        page_cart.click_payment_info_continue_button()
        page_cart.click_confirm_button()
        # plus function to check whether we see something after checkcout confirmation




    def tearDown(self) -> None:
       self.driver.quit()


if __name__ == "__main__":
    unittest.main()
