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


@pytest.mark.usefixtures('create_resource')
class TestHomeNative(softest.TestCase):
    '''
    Test Class for home Page
    '''

    @allure.issue(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia"
                      "%20Cookies/_workitems"
                      "/edit/2309", name="Rename primary navigation item")
    @allure.description("Given the Customer is on the Home page\
                        \nThen the customer"
                        " should see Menu instead of Our Menu")
    def test_signup(self):
        login_obj = self.home_obj.click_login_icn()
        signup_obj = login_obj.click_sign_up_btn()
        signup_obj.enter_email_address(const.email)
        signup_obj.enter_password(const.pwd)
        signup_obj.confirm_password(const.pwd)
        signup_obj.click_create_account_btn()
        login_obj = self.home_obj.click_login_icn()
        login_txt = login_obj.get_login_page_text()
        self.soft_assert(self.assertIn, "You have", login_txt, "Text not same")
        PageBase.scroll_to_bottom(self)
        email = login_obj.get_email_address()
        self.soft_assert(
            self.assertEqual,
            email,
            const.email,
            "account not created")
        self.assert_all()

    @pytest.mark.run(order=3)
    def test_get_loyalty_points(self):
        login_obj = self.home_obj.click_login_icn()
        login_obj.enter_username(const.uname)
        login_obj.enter_password(const.password)
        login_obj.click_login()
        login_obj = self.home_obj.click_login_icn()
        points = login_obj.get_loyalty_points()
        self.soft_assert(self.assertIn, "0", points, "points dont match")
        self.assert_all()

    @pytest.mark.run(order=4)
    def test_profile(self):
        login_obj = self.home_obj.click_login_icn()
        login_obj.enter_username(const.uname)
        login_obj.enter_password(const.password)
        login_obj.click_login()
        login_obj = self.home_obj.click_login_icn()
        PageBase.scroll_to_bottom(self)
        profile_obj = login_obj.click_edit_profile()
        profile_obj.enter_first_name(const.first_name_edit)
        self.driver.hide_keyboard()
        profile_obj.enter_email(const.email_edit)
        profile_obj.enter_mobile(const.mobile_number)
        PageBase.scroll_to_bottom(self)
        profile_obj.click_save_btn()
        first_name = login_obj.get_first_name()
        self.soft_assert(
            self.assertEqual,
            first_name,
            const.first_name_edit,
            "First name not updated")
        email = login_obj.get_email_address()
        self.soft_assert(
            self.assertEqual,
            email,
            const.email_edit,
            "Email not updated")
        profile_obj = login_obj.click_edit_profile()
        profile_obj.enter_email(const.uname)
        PageBase.scroll_to_bottom(self)
        profile_obj.click_save_btn()
        self.assert_all()

    @pytest.mark.run(order=7)
    def test_logout(self):
        login_obj = self.home_obj.click_login_icn()
        login_obj.enter_username(const.uname)
        login_obj.enter_password(const.password)
        login_obj.click_login()
        login_obj = self.home_obj.click_login_icn()
        login_txt = login_obj.get_login_page_text()
        self.soft_assert(self.assertIn, "You have", login_txt, "Text not same")
        PageBase.scroll_to_bottom(self)
        PageBase.scroll_to_bottom(self)
        login_obj.click_logout()
        login_obj.click_confirm_logout()
        self.home_obj.click_login_icn()
        self.assert_all()

    def test_close_account(self):
        login_obj = self.home_obj.click_login_icn()
        login_obj.enter_username(const.uname)
        login_obj.enter_password(const.password)
        login_obj.click_login()
        login_obj = self.home_obj.click_login_icn()
        login_txt = login_obj.get_login_page_text()
        self.soft_assert(self.assertIn, "You have", login_txt, "Text not same")
        PageBase.scroll_to_bottom(self)
        PageBase.scroll_to_bottom(self)
        login_obj.click_close_account()
        login_obj.click_confirm_close_account()
        self.home_obj.click_login_icn()
        self.assert_all()
