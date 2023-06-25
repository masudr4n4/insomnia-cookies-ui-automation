import allure
from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
from WebLocators import SignUpPageLocators as loc
log = cl.customLogger(logging.INFO)


class SignUpPage(PageBase):
    """
    Class for methods of SignUp Page of mobile view
    """

    def __init__(self, driver, cwd):
        super().__init__(driver)
        self.cwd = cwd
        self.driver.implicitly_wait(10)

    @allure.step("enter email address")
    def enter_email_address(self, email):
        """
        Method to enter the email address
        :param email:
        :return:
        """
        try:
            log.info("Entering the email address")
            locator = self.get_locator_wrt_directory(
                loc, "input_email", self.cwd)
            self.send_keys(locator, email)
        except Exception as e:
            raise Exception(
                "Unable to enter the email address due to " + str(e))

    @allure.step("enter password")
    def enter_password(self, pwd):
        """
        Method to enter the password
        :param pwd:
        :return:
        """
        try:
            log.info("Entering the password")
            locator = self.get_locator_wrt_directory(
                loc, "input_password", self.cwd)
            self.send_keys(locator, pwd)
        except Exception as e:
            raise Exception("Unable to enter the password due to " + str(e))

    @allure.step("confirm password")
    def confirm_password(self, pwd):
        """
        Method to confirm the password
        :param pwd:
        :return:
        """
        try:
            log.info("Re-Entering the password to confirm password")
            locator = self.get_locator_wrt_directory(
                loc, "confirm_password", self.cwd)
            self.send_keys(locator, pwd)
        except Exception as e:
            raise Exception("Unable to Confirm the password due to " + str(e))

    @allure.step("Clicking create account button")
    def click_create_account(self):
        """
        Method to click on create account button
        :return:
        """
        try:
            log.info("Clicking on create account button")
            locator = self.get_locator_wrt_directory(
                loc, "create_account_btn", self.cwd)
            self.wait_till_element_is_present(locator)
            self.click(locator)

        except Exception as e:
            raise Exception(
                "Unable to click on create account button due to " + str(e))

    @allure.step("Clicking already have login button")
    def click_already_have_login_btn(self):
        """
        Method to click on already have login btn
        :return:
        """
        try:
            log.info("Clicking on already have login button")
            locator = self.get_locator_wrt_directory(
                loc, "already_login_btn", self.cwd)
            self.wait_till_element_is_present(locator)
            self.click(locator)
        except Exception as e:
            raise Exception(
                "Unable to click on already have login button due to " +
                str(e))

    @allure.step("Clicking sign up from fcebook")
    def click_sign_up_facebook_btn(self):
        """
        Method to click on Sign Up using facebook btn
        :return:
        """
        try:
            log.info("Clicking on Sign Up from Facebook button")
            locator = self.get_locator_wrt_directory(
                loc, "sign_up_facebook_btn", self.cwd)
            self.wait_till_element_is_present(locator)
            self.click(locator)
        except Exception as e:
            raise Exception(
                "Unable to click on Sign Up from facebook button due to " +
                str(e))
