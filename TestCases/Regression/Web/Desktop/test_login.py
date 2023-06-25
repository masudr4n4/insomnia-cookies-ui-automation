import pytest
import logging
import softest
import allure
import Utilities.CustomLogger as cl

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestLogin(softest.TestCase):

    @allure.story('Login Section: FB login')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select the Login
    Then Login page opens
    And user clicks facebook login button
    Then Facebook should open:
    https://www.facebook.com""")
    def test_2355_Login_Insomnia_Facebook(self):
        self.home_obj.wait_for_menu_to_load()
        login_obj = self.home_obj.click_header_login()
        login_obj.click_facebook_login()
        handle = self.footer_obj.wait_till_method(
            self.footer_obj.handle_exists(1))
        self.footer_obj.switch_to_new_window(handle)
        self.footer_obj.verify_facebook_page()
