import time
import allure
from Utilities.PageBase import PageBase
import logging
import Utilities.CustomLogger as cl
from WebLocators import LoginPageLocators as loc
log = cl.customLogger(logging.INFO)


class LoginPage(PageBase):
    """
    Class for methods of Login Page
    """

    def __init__(self, driver, cwd):
        super().__init__(driver)
        self.cwd = cwd
        self.driver.implicitly_wait(10)

    @allure.step("Entering the username")
    def enter_username(self, username):
        """
        Method to enter the username on login page
        :param username:
        :return:
        """
        try:
            log.info("Entering the username in the input box")
            locator = self.get_locator_wrt_directory(
                loc, "input_uname", self.cwd)
            self.wait_till_element_is_present(locator)
            self.send_keys(locator, username)
        except Exception as e:
            raise Exception("Unable to enter the username due to " + str(e))

    def click_facebook_login(self):
        """
        Method to click the Facebook icon
        """
        try:
            log.info("Clicking on Facebook icon in footer")
            locator = self.get_locator_wrt_directory(
                loc, "btn_login_fb", self.cwd)
            self.click(self.wait_till_element_is_clickable(locator))
        except Exception as e:
            raise Exception("Unable to click fb login button due to " + str(e))

    @allure.step("Entering the password")
    def enter_password(self, password):
        """
        Method the enter the password on login page
        :param password:
        :return:
        """
        try:
            log.info("Entering the password in the input box")
            locator = self.get_locator_wrt_directory(
                loc, "input_pwd", self.cwd)
            self.wait_till_element_is_present(locator)
            self.send_keys(locator, password)
        except Exception as e:
            raise Exception("Unable to enter the password due to " + str(e))

    def click_forgot_password(self):
        """
        Method to click the forgot password link
        :return:
        """
        try:
            log.info("Clicking the forgot password link")
            locator = self.get_locator_wrt_directory(
                loc, "forgot_pwd_link", self.cwd)
            self.wait_till_element_is_present(locator)
            self.click(locator)
        except Exception as e:
            raise Exception(
                "Unable to click on forgot password link due to " + str(e))

    @allure.step("Clicking the login button")
    def click_login(self):
        """
        Method to click Login  button
        :return:
        """
        try:
            log.info("Clicking the login button")
            locator = self.get_locator_wrt_directory(
                loc, "login_btn", self.cwd)
            self.wait_till_element_is_clickable(locator)
            self.click(locator)
        except Exception as e:
            raise Exception("Unable to click login  button due to " + str(e))

    def click_login_with_facebook(self):
        """
        Method to click Login with facebook button
        :return:
        """
        try:
            log.info("Clicking the login with facebook button")
            locator = self.get_locator_wrt_directory(
                loc, "btn_login_fb", self.cwd)
            self.wait_till_element_is_present(locator)
            self.click(locator)
        except Exception as e:
            raise Exception(
                "Unable to click login with facebook button due to " + str(e))

    def verify_error_message_is_displayed(self):
        """
        Method to verify if validation error message is displayed
        """
        try:
            locator = self.get_locator_wrt_directory(
                loc, "error_img", self.cwd)
            flag = False
            if self.wait_till_element_is_visible(locator):
                flag = True
            return flag
        except Exception as e:
            raise Exception(
                "Unable to check if validation error message is displayed due to " +
                str(e))
