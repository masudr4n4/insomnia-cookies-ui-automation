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
    def test_click_make_a_btn(self):
        self.home_obj.click_make_a_box_btn()
