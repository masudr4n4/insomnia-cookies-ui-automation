from Utilities.PageBase import PageBase
import logging
from NativeAppsLocators import SignUpPageLocators as loc
import Utilities.CustomLogger as Cl
log = Cl.customLogger(logging.INFO)


class NativeSignUpPage(PageBase):
    """
    Class for methods of Home Page for Native apps
    """
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_address(self, email):
        '''
        Method to enter the email address
        :param email:
        :return:
        '''
        try:
            log.info("Entering the email address")
            self.wait_till_element_is_present(loc.input_email_android)
            self.send_keys(loc.input_email_android, email)
            self.hide_keyboard()
        except Exception as e:
            raise Exception(
                "Unable to enter the email address due to " + str(e))

    def enter_password(self, pwd):
        '''
        Method to enter the password
        :param email:
        :return:
        '''
        try:
            log.info("Entering the password")
            self.wait_till_element_is_present(loc.input_pwd_android)
            self.send_keys(loc.input_pwd_android, pwd)
            self.hide_keyboard()
        except Exception as e:
            raise Exception("Unable to enter the password due to " + str(e))

    def confirm_password(self, pwd):
        '''
        Method to confirm the password
        :param email:
        :return:
        '''
        try:
            log.info("Confirming the password")
            self.wait_till_element_is_present(loc.confirm_pwd_android)
            self.send_keys(loc.confirm_pwd_android, pwd)
            self.hide_keyboard()
        except Exception as e:
            raise Exception("Unable to Confirm the password due to " + str(e))

    def click_create_account_btn(self):
        '''
        Method to click create account button
        :return:
        '''
        try:
            log.info("Clicking the create account button")
            self.wait_till_element_is_present(loc.create_acc_btn_android)
            self.click(loc.create_acc_btn_android)
        except Exception as e:
            raise Exception(
                "Unable to click on create account button due to " + str(e))
