import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
from Utilities.PageBase import PageBase
import softest
import time
import allure

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestHome(softest.TestCase):
    """
    Test Class for home Page
    """

    def test_2348_signup_functionality(self):
        """
        Testcase for Signup functionality
        """
        self.home_obj.wait_for_menu_to_load()
        sign_up_obj = self.home_obj.click_sign_me_up_btn()
        sign_up_obj.enter_email_address(self.home_obj.get_random_email())
        self.sign_up_obj.enter_password(const.pwd)
        self.sign_up_obj.confirm_password(const.pwd)
        self.sign_up_obj.click_create_account()
        flag = self.home_obj.is_user_logged_in()
        self.soft_assert(self.assertTrue, flag, "Account not created")
        self.assert_all()

    def test_QA_TASK_2448_TC1_geolocation_store(self):
        """
        Test case for QA Task 2448
        """
        driver = self.home_obj.change_location(self.latitude, self.longitude)
        self.driver = driver
        location_obj = self.home_obj.click_locations_header()
        location_obj.click_locate_on_map_icn()
        flag = location_obj.is_location_list_present()
        self.soft_assert(self.assertTrue, flag, "Location list not found")

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2736")
    @allure.story('Clicking on "Join now" button on home page should redirect to create-account page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                UAC: Clicking on "Join now" button on home page should redirect to create-account page
                                Given User is on home page
                                When the user click "Join now" button in 'Start earning dough' section
                                Then user should get redirected to 'create-account' page​""")
    def test_2736_click_join_now(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_join_now_btn()
        flag2 = self.home_obj.verify_create_account_page_opens()
        self.soft_assert(
            self.assertTrue,
            flag2,
            "unable to open create account page")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/3298")
    @allure.story("User is able to Edit the profile")
    @allure.description("""
        Login to the insomnia cookies website.
        Click on Login button again to see the user profile
        Click on Edit button
        Enter the user details (First Name, Last Name, Mobile number , Email address)
        Click on Save button
        Verify the details have been updated on the profile page""")
    @pytest.mark.usefixtures('login_to_edit')
    @pytest.mark.usefixtures('create_resource')
    def test_edit_user_profile(self):
        self.home_obj.wait_for_menu_to_load()
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.click_edit_profile_lnk()
        profile_obj.enter_first_name(const.first_name)
        profile_obj.enter_last_name(const.last_name)
        profile_obj.enter_mobile_number(const.mobile_number)
        profile_obj.enter_email_address(const.uname2)
        profile_obj.click_save_changes()
        f_name = profile_obj.get_first_name()
        self.soft_assert(
            self.assertEqual,
            f_name,
            const.first_name,
            "First name didn't update")
        l_name = profile_obj.get_last_name()
        self.soft_assert(
            self.assertEqual,
            l_name,
            const.last_name,
            "Last name didn't update")
        email = profile_obj.get_email_address()
        self.soft_assert(
            self.assertEqual,
            email,
            const.uname2,
            "Email didn't update")
        profile_obj.click_logout_btn()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/4215")
    @allure.story("View order history")
    @allure.description("""
            Given User logs in into the website
            When user clicks the profile icon
            And click the see all orders link
            Then verify order history page opens with previous order details""")
    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('create_resource')
    def test_4215_see_order_history(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"],
            user="LoggedIn")
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.click_see_all_orders()
        boolean = profile_obj.verify_order_history_displayed()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order history page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/4239")
    @allure.story("View order details")
    @allure.description("""
                Given User logs in into the website
                When user clicks the profile icon
                And click the view order details link
                Then verify order details page opens with recent order details""")
    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('create_resource')
    def test_4239_see_order_details(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_select_address_btn()
        self.home_obj.enter_and_select_delivery_address(
            const.location_page_dict["TestStore"])
        product_obj = self.home_obj.click_product(
            product_type="box", product_number=2)
        product_obj.click_pick_for_me()
        product_obj.click_add_to_order_btn()
        self.home_obj.is_item_Added()
        product_obj.click_cart_btn(1)
        checkout_obj = product_obj.click_review_order_btn()
        checkout_obj.click_delivery_time()
        checkout_obj.select_date_from_dropdown(1)
        checkout_obj.select_time_from_dropdown(1)
        checkout_obj.click_select_button()
        checkout_obj.click_contact_info(4)
        checkout_obj.enter_and_add_contact_details(
            const.checkout_page_dict["firstName"],
            const.checkout_page_dict["lastName"],
            const.checkout_page_dict["phoneNumber"],
            const.checkout_page_dict["email"],
            user="LoggedIn")
        checkout_obj.click_choose_a_payment_method(5)
        checkout_obj.enter_cc_dc_details_and_Add_card(
            const.checkout_page_dict["cardHolderName"],
            const.checkout_page_dict["cardNumber"],
            const.checkout_page_dict["expirationDate"],
            const.checkout_page_dict["cvvNumber"],
            const.checkout_page_dict["zipCode"])
        checkout_obj.click_place_order_btn()
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.click_view_order_details()
        boolean = profile_obj.verify_order_details_displayed()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Order details page not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/4360")
    @allure.story("View order details")
    @allure.description("""
                        Given User logs in into the website
                        When user clicks the logout button
                        And click the confirm logout button
                        Then user should get logged out""")
    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('create_resource')
    def test_4360_logout(self):
        self.home_obj.wait_for_menu_to_load()
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.click_logout_btn()
        profile_obj.click_confirm_logout()
        boolean = profile_obj.verify_user_details_not_displayed()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "User details still visible user unable to logout")

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/4407")
    @allure.story("Deactivate account")
    @allure.description("""
                    Given User signs-up and login in into the website
                    When user clicks the profile icon
                    And click deactivate account
                    And click confirm Deactivate account
                    Then user should logout
                    When user tries to login again with same credentials
                    Then verify failed login validation error message is displayed""")
    def test_4407_deactivate_account(self):
        """
        Testcase for deactivating account
        """
        self.home_obj.wait_for_menu_to_load()
        sign_up_obj = self.home_obj.click_sign_me_up_btn()
        email = self.home_obj.get_random_email()
        sign_up_obj.enter_email_address(email)
        self.sign_up_obj.enter_password(const.pwd)
        self.sign_up_obj.confirm_password(const.pwd)
        self.sign_up_obj.click_create_account()
        flag = self.home_obj.is_user_logged_in()
        self.soft_assert(self.assertTrue, flag, "Account not created")
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.deactivate_account()
        profile_obj.click_confirm_deactivate_account()
        login_obj = self.home_obj.click_header_login()
        login_obj.enter_username(email)
        login_obj.enter_password(const.pwd)
        login_obj.click_login()
        boolean = login_obj.verify_error_message_is_displayed()
        self.soft_assert(
            self.assertTrue,
            boolean,
            "Validation error message not displayed")
        self.assert_all()
