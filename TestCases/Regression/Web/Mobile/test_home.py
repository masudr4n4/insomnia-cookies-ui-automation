import pytest
import Utilities.CustomLogger as Cl
import Static.Constants as const
import logging
import softest
import allure

log = Cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestHome(softest.TestCase):
    """
    Test Class for SignUp Page
    """

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

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/5464")
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
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        profile_obj = mobile_menu_obj.click_locations_mobile_menu()
        profile_obj = self.home_obj.click_header_login(loggedIn=True)
        profile_obj.click_edit_profile_lnk()
        profile_obj.enter_first_name(const.first_name)
        profile_obj.enter_last_name(const.last_name)
        profile_obj.enter_email_address(const.uname2)
        profile_obj.enter_mobile_number(const.mobile_number)
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
