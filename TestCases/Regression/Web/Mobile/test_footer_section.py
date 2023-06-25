import Utilities.CustomLogger as cl
import pytest
import logging
import softest
import allure
import time

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestFooter(softest.TestCase):
    """
    Test Class for Footer section
    """

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Newsroom page')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Newsroom from <location>
    Then the Newsroom page should open:
    https://insomniacookies.com/newsroom

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2610_Newsroom(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_newsroom_mobile_menu()
        self.footer_obj.verify_newsroom_insomnia()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: FAQ')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select FAQ from <location>
    Then the FAQ page should open

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2611_FAQ(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_FAQ_mobile_menu()
        self.footer_obj.verify_faq_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Privacy Policy')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Privacy Policy from <location>
    Then the Privacy Policy page should open

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2612_Privacy_Policy(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_privacy_policy_mobile_menu()
        self.footer_obj.verify_privacy_policy_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Terms and Conditions')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Terms and Conditions from <location>
    Then the Terms and Conditions page should open

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2613_Terms_and_Conditions(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_terms_conditions_mobile_menu()
        self.footer_obj.verify_terms_and_condition_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Accessibility')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Accessibility from <location>
    Then the Accessibility page should open

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2614_Accessibility(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_accessibility_mobile_menu()
        self.footer_obj.verify_accessibility_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: About Us')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select About Us from <location>
    Then the About Us page should open

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2616_About_Us(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_about_us_mobile_menu()
        self.footer_obj.verify_about_us_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Careers')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Careers from <location>
    Then the Careers page should open:
    https://careers.insomniacookies.com/

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2617_Careers(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_careers_mobile_menu()
        self.footer_obj.verify_career_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Donations')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select Donations from <location>
    Then the Donations page should open:
    https://insomniacookies.com/donations

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2618_Donations(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_donations_mobile_menu()
        self.footer_obj.verify_donation_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Social media links')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select the Instagram icon from <location>
    Then the Insomnia Cookies page should open:
    https://www.instagram.com/insomniacookies/

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2634_Open_Insomnia_Instagram(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_instagram_mobile_menu()
        mobile_menu_obj.switch_to_new_window(
            mobile_menu_obj.get_window_handles()[-1])
        self.footer_obj.verify_instagram_page()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2631")
    @allure.story('Footer Section: Social media links')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Given the user is on the home page
    When they select the Facebook icon from <location>
    Then the Insomnia Cookies page should open:
    https://www.facebook.com/insomniacookies

    |   location|
    |     Footer|
    |Mobile Menu|""")
    def test_2635_Open_Insomnia_Facebook(self):
        self.home_obj.wait_for_menu_to_load()
        mobile_menu_obj = self.home_obj.click_hamburger_menu()
        mobile_menu_obj.click_facebook_mobile_menu()
        mobile_menu_obj.switch_to_new_window(
            mobile_menu_obj.get_window_handles()[-1])
        self.footer_obj.verify_facebook_page()
