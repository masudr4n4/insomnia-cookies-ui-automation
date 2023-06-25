import pytest
import Utilities.CustomLogger as cl
import Static.Constants as const
import logging
import softest
import time
import allure

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.regression
@pytest.mark.usefixtures('create_resource')
class TestContact(softest.TestCase):
    """
    Test Class for Contact Page
    """

    @allure.story('Open contact Us page from HomePage Scenario')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
            1. Open the website
            2. Click on Contact link from footer on HomePage
            3. Click on Feedback button to expand the drop down list
            4. Click on the General Inquiries option
            5. Enter full name
            6. Select Store""")
    def test_contact(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        contact_obj.click_generalInquiries()
        contact_obj.enter_fullname(const.fullname)
        contact_obj.select_store()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2681")
    @allure.story('Open Contact us page and fill Feedback form')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                        Given the User in on homepage
                        When user click on Contact link from footer on HomePage
                        Then the Contact page should open
                        When in feedback form enter order number
                        And enter full name
                        And enter email address
                        And enter mobile number
                        And select Store
                        And leave a comment
                        And user click Submit button
                        Then verify form should get submitted""")
    def test_2681_fill_feedback_form(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        flag = contact_obj.verify_contact_us_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on contact US page")
        contact_obj.enter_order_number(const.contact_page_dict["orderNumber"])
        contact_obj.enter_fullname(const.contact_page_dict["fullName"])
        contact_obj.enter_email(const.contact_page_dict["emailAddress"])
        contact_obj.enter_mobileNumber(const.contact_page_dict["mobileNumber"])
        contact_obj.select_store()
        contact_obj.enter_comment(const.contact_page_dict["comment"])
        contact_obj.click_submit_button()
        actualText = contact_obj.get_success_message_text()
        expectedText = "Form successfully submitted!"
        self.soft_assert(
            self.assertEqual,
            actualText,
            expectedText,
            "submit success message not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2773")
    @allure.story('Open Contact us page and fill and submit events form')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given the User in on homepage
                            When user click on Contact link from footer on HomePage
                            Then the Contact page should open
                            When use clicks on Feedback button to expand the drop down list
                            And Click on the Events option
                            Then book an event page should open
                            When user enter the Full Name
                            And enter the email address
                            And enter the organization name
                            And enter the mobile number
                            And enter the event location
                            And enter the event date
                            And enter the event type
                            And enter the comment
                            And click submit button
                            Then verify form should get submitted successfully""")
    def test_2773_fill_events_form(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        contact_obj.click_eventsButton()
        flag = contact_obj.verify_events_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on events page")
        contact_obj.enter_events_Form_fullname(
            const.contact_page_dict["fullName"])
        contact_obj.enter_email(const.contact_page_dict["emailAddress"])
        contact_obj.enter_organisationName(
            const.contact_page_dict["organisationName"])
        contact_obj.enter_mobileNumber(const.contact_page_dict["mobileNumber"])
        contact_obj.enter_eventLocation(
            const.contact_page_dict["eventLocation"])
        contact_obj.enter_eventDate(const.contact_page_dict["eventDate"])
        contact_obj.enter_eventType(const.contact_page_dict["eventType"])
        contact_obj.enter_comment(const.contact_page_dict["comment"])
        contact_obj.click_submit_button()
        actualText = contact_obj.get_success_message_text()
        expectedText = "Form successfully submitted!"
        self.soft_assert(
            self.assertEqual,
            actualText,
            expectedText,
            "submit success message not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2682")
    @allure.story('Open Contact us page and fill General Inquiries form')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                    Given the User in on homepage
                    When user click on Contact link from footer on HomePage
                    Then the Contact page should open
                    When use clicks on Feedback button to expand the drop down list
                    And Click on the General Inquiries option
                    And enter full name
                    And select Store
                    And enter email address
                    And enter mobile number
                    And leave a comment
                    And user click Submit button
                    Then verify form should get submitted""")
    def test_2682_general_inquiries_form(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        flag = contact_obj.verify_contact_us_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on contact US page")
        contact_obj.click_generalInquiries()
        contact_obj.enter_fullname(const.contact_page_dict["fullName"])
        contact_obj.select_store()
        contact_obj.enter_email(const.contact_page_dict["emailAddress"])
        contact_obj.enter_mobileNumber(const.contact_page_dict["mobileNumber"])
        contact_obj.enter_comment(const.contact_page_dict["comment"])
        contact_obj.click_submit_button()
        actualText = contact_obj.get_success_message_text()
        expectedText = "Form successfully submitted!"
        self.soft_assert(
            self.assertEqual,
            actualText,
            expectedText,
            "submit success message not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2872")
    @allure.story('Open Contact us page and fill and submit Real Estate form')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                        Given the User in on homepage
                        When user click on Contact link from footer on HomePage
                        Then the Contact page should open
                        When use clicks on Feedback button to expand the drop down list
                        And Click on the Real Estate option
                        And enter full name
                        And enter email address
                        And leave a comment
                        And user click Submit button
                        Then verify form should get submitted""")
    def test_2872_real_estate_form(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        flag = contact_obj.verify_contact_us_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on contact US page")
        contact_obj.click_realEstate()
        contact_obj.enter_fullname(const.contact_page_dict["fullName"])
        contact_obj.enter_email(const.contact_page_dict["emailAddress"])
        contact_obj.enter_proposed_location(
            const.contact_page_dict["proposedLocation"])
        contact_obj.enter_comment(const.contact_page_dict["comment"])
        contact_obj.click_submit_button()
        actualText = contact_obj.get_success_message_text()
        expectedText = "Form successfully submitted!"
        self.soft_assert(
            self.assertEqual,
            actualText,
            expectedText,
            "submit success message not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2873")
    @allure.story('Open Contact us page and fill and submit vendor form')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                            Given the User in on homepage
                            When user click on Contact link from footer on HomePage
                            Then the Contact page should open
                            When user clicks on Feedback button to expand the drop down list
                            And Click on the Vendor option
                            And enter Organisation name
                            And enter email address
                            And enter phone number
                            And enter product name
                            And enter product cost
                            And leave a comment
                            And user click Submit button
                            Then verify form should get submitted""")
    def test_2873_vendor_form(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        flag = contact_obj.verify_contact_us_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on contact US page")
        contact_obj.click_vendor()
        contact_obj.enter_organisationName(
            const.contact_page_dict["organisationName"])
        contact_obj.enter_email(const.contact_page_dict["emailAddress"])
        contact_obj.enter_phoneNumber(const.contact_page_dict["phoneNumber"])
        contact_obj.enter_product_name(const.contact_page_dict["productName"])
        contact_obj.enter_product_cost(const.contact_page_dict["productCost"])
        contact_obj.enter_comment(const.contact_page_dict["comment"])
        contact_obj.click_submit_button()
        actualText = contact_obj.get_success_message_text()
        expectedText = "Form successfully submitted!"
        self.soft_assert(
            self.assertEqual,
            actualText,
            expectedText,
            "submit success message not displayed")
        self.assert_all()

    @allure.link(url="https://dev.azure.com/InsomniaCookiesDev/Insomnia%20Cookies/_workitems/edit/2773")
    @allure.story('Open Contact us page and open press page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
                                Given the User in on homepage
                                When user click on Contact link from footer on HomePage
                                Then the Contact page should open
                                When user clicks on Feedback button to expand the drop down list
                                And Click on the Vendor option
                                When click on Press option
                                Then verify marketing email ID is displayed""")
    def test_2773_press(self):
        self.home_obj.wait_for_menu_to_load()
        self.home_obj.click_hamburger_menu()
        contact_obj = self.footer_obj.click_footer_contact()
        contact_obj.click_feedback()
        flag = contact_obj.verify_contact_us_page_opens()
        self.soft_assert(self.assertTrue, flag, "not on contact US page")
        contact_obj.click_press()
        isMarketingID_displayed = contact_obj.is_marketing_ID_displayed()
        self.soft_assert(
            self.assertTrue,
            isMarketingID_displayed,
            "marketing email ID not displayed")
        self.assert_all()
