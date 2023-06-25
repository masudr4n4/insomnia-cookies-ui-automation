import pytest
import Utilities.CustomLogger as cl
import logging
import softest
import Static.Constants as const
import time
import allure
from Utilities.PageBase import PageBase

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.usefixtures('create_resource')
class TestMenuNative(softest.TestCase):
    '''
    Test Class for Menu Page
    '''

    def test_click_profile_link(self):
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_privacy_policy()
        flag2 = login_obj.verify_privacy_policy_banner()
        self.soft_assert(
            self.assertTrue,
            flag2,
            "privacy policy banner not displayed")
        self.assert_all()

    def test_click_terms_condition_link(self):
        login_obj = self.home_obj.click_hamburger_menu()
        login_obj.click_terms_condition()
        flag2 = login_obj.verify_terms_condition_banner()
        self.soft_assert(
            self.assertTrue,
            flag2,
            "Terms and condition banner not displayed")
        self.assert_all()
