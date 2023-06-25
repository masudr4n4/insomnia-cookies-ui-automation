import json
import logging
import os
import random
import time
from enum import Enum
from urllib.parse import unquote
import Static.Constants as const
from retry import retry
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, ElementClickInterceptedException
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import Utilities.CustomLogger as cl


class PageBase:
    log = cl.customLogger(logging.INFO)
    timeout = 30

    def __init__(self, driver):
        self.driver = driver

    def open(self, url, wait_time=2):
        """
        Visit the page base_url + url
        :param url: URL to be opened
        :param wait_time: time to wait till url opens
        :return:
        """
        if self.driver.current_url != url:
            self.driver.get(url)

    def get_page_source(self):
        """
        Return the page source of current page
        :return:
        """
        return self.driver.page_source

    def wait_for_page_load(self, timeout=10):
        self.log.debug(
            "Waiting for page to load at {}.".format(
                self.driver.current_url))
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self, timeout).until(staleness_of(old_page))

    def wait_for_element_to_be_staleness(self, locator, timeout=10):
        element = self.find_element(locator)
        yield
        WebDriverWait(self, timeout).until(staleness_of(element))

    def get_currentdriver(self):
        """
        Return current driver
        :return: current driver instance
        """
        return self.driver

    def get_current_title(self):
        """
        Get the current title of the opened browser
        :return: current browser title
        """
        return self.driver.title

    def get_current_url(self):
        """
        Get the current URL
        :return: Return current URL
        """
        return self.driver.current_url

    def is_element_selected(self, locator):
        """
        Check whether provided element is selected
        :param locator: Element locator strategy
        :return: True or False about the element selection
        """
        element = self.find_element(locator)
        return element.is_selected()

    def is_element_enabled(self, locator):
        """
        Returns whether given element is enabled or not
        :param locator: Element locator strategy
        :return: True if given element is enabled else returns false
        """
        element = self.find_element(locator)
        return element.is_enabled()

    @retry(StaleElementReferenceException, tries=1)
    def click(self, locator):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("""
                            var element = arguments[0];
                            element.click();
                            """, element)
        else:
            raise Exception("Could not click on locator " + element)

    def javascript_click(self, locator):
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise Exception("Could not click on locator " + element)

    def set_field(self, locator, element_value):
        """
        Locates the element by specified locator and then sets its value
        :param locator: Element locator strategy
        :param element_value: value to be written
        :return: element
        """
        webelement = self.find_element(locator)
        try:
            webelement.send_keys(element_value)
        except Exception as e:
            raise Exception("Could not write on the the element {} due to {}".
                            format(webelement, e))

        return webelement

    def get_text(self, locator):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        element = self.find_element(locator)
        return element.text

    def get_element_text(self, element):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        return element.text

    def is_element_displayed(self, locator):
        """
        Returns whether given element is displayed or no
        :param locator: Element locator strategy
        :return: True if given element is displayed else returns false
        """
        element = self.find_element(locator)
        return element.is_displayed()

    def switch_to_frame(self, frame_id):
        """
        Switch to the given frame based on id
        :param frame_id: id of the frame (can be xpath also)
        :return:
        """
        self.driver.switch_to_frame(frame_id)

    def switch_to_main_window(self):
        """
        Switch to the main browser window
        :return:
        """
        self.driver.switch_to_default_content()

    def move_and_click(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param locator: Element locator strategy
        :return: element
        """
        self.wait_till_element_is_visible(locator)
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception(
                "Could Not click locator {} due to {}".format(
                    element, e))
        return element

    def click_and_move_by_offset(self, locator, offset):
        element = self.find_element(locator)
        drawing = ActionChains(self.driver) \
            .move_to_element(element) \
            .click_and_hold(element) \
            .move_by_offset(*offset) \
            .release()
        drawing.perform()

    @retry(NoSuchElementException, tries=1)
    def find_element(self, locator):
        """
        Find and return element based on the given locator value
        E.g: draggableElement = ("xpath@@//div[@id='draggable']")
        :param locator: Element locator strategy
        :return: Element
        """
        return self.driver.find_element(
            *self.__get_by(locator_with_strategy=locator))

    def find_child_element(self, element, locator):
        by = self.__get_by(locator_with_strategy=locator)
        return element.find_element(*by)

    def find_child_elements(self, element, locator):
        by = self.__get_by(locator_with_strategy=locator)
        return element.find_elements(*by)

    def __get_by(self, locator_with_strategy):
        """
        Get and return By instance based on the locator strategy
        :param locator_with_strategy: Element locator strategy
        :return: By instance of the element
        """
        if "@@" not in locator_with_strategy:
            locator_with_strategy = Strategy.ID.value + "@@" + locator_with_strategy

        strategy_and_locator = str(locator_with_strategy).split("@@")
        strategy = strategy_and_locator[0]
        locator = strategy_and_locator[1]
        by = None
        if strategy == Strategy.XPATH.value:
            by = (By.XPATH, locator)
        elif strategy == Strategy.ID.value:
            by = (By.ID, locator)
        elif strategy == Strategy.CSS.value:
            by = (By.CSS_SELECTOR, locator)
        elif strategy == Strategy.TAGNAME.value:
            by = (By.TAG_NAME, locator)
        return by

    def find_elements(self, locator):
        """
        Find and return the list of webelements based on the given locator value
        :param locator: Element locator strategy
        :return: list of the elements
        """
        return self.driver.find_elements(
            *self.__get_by(locator_with_strategy=locator))

    @retry(StaleElementReferenceException, tries=1)
    def get_attribute(self, locator, attribute):
        """
        Get the provided attribute value for the given element
        :param locator: Element locator strategy
        :param attribute: attribute
        :return: value of the attribute
        """
        if isinstance(locator, WebElement):
            return locator.get_attribute(attribute)
        else:
            element = self.find_element(locator)
            return element.get_attribute(attribute)

    @retry(StaleElementReferenceException, tries=1)
    def get_text(self, locator):
        """
        Get the text value for the given element
        :param locator: Element locator strategy
        :return: text of the attribute
        """
        if isinstance(locator, WebElement):
            return locator.text

    def drag_and_drop(self, draggable, droppable):
        """
        Performs drag and drop action using selenium action class
        :param draggable: draggable element
        :param droppable: droppable element
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.drag_and_drop(draggable, droppable).perform()
        except Exception as e:
            raise e

    def select_value_from_dropdown(self, locator, value):
        """
        It will select value from dropdown based on visible text
        :param locator: dropdwon Element locator strategy
        :return:
        """
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)

    def select_value_from_dropdown_by_index(self, locator, index):
        """
        It will select first value from dropdown
        :param locator: dropdwon Element locator strategy
        :param index: index of the dropdown element
        :return:
        """
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_index(index)

    def explicit_wait(self, locator):
        """
        Smart Wait in Selenium, wait till element is clickable
        :param locator: Element locator strategy
        :return: Found Element
        """
        element = self.find_element(locator)
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.element_to_be_clickable(element))
        except Exception as e:
            raise e
        return element

    def select_dropdown_option(self, locator, option_text):
        """
        Selects the option in the drop-down based on the tag text
        :param locator: element
        :param option_text: value to be selected
        :return:
        """
        dropdown = self.find_element(locator)
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

    def hit_enter(self, locator, wait_time=2):
        """
        Hit Enter
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ENTER)
        except Exception as e:
            raise e

    def send_keys(self, locator, *keys):
        """
        send keys to locator
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(*(keys))
        except Exception as e:
            raise e

    def check_existence(self, locator):
        try:
            self.driver.find_element(
                *self.__get_by(locator_with_strategy=locator))
            return True
        except Exception as e:
            return False

    def wait_for_element_custom(self, locator):
        count = 0
        flag = False
        while count < 30:
            count = count + 1
            if self.check_existence(locator) is True:
                flag = True
                break
        if not flag:
            print('Element is not loaded: ' + str(locator))
        else:
            print('Element found!')

    def wait_till_all_elements_are_present(self, locator, timeout=timeout):
        """
        WebDriver Explicit wait till all elements are present
        :param locator: elements to be checked
        :param timeout: timeout
        :return:
        """
        try:
            elements = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=2,
                ignored_exceptions=NoSuchElementException).until(
                EC.presence_of_all_elements_located(
                    self.__get_by(locator)))
            return elements
        except Exception as e:
            raise e

    def validate_text_in_element(self, locator, text):
        """
        Validate the text in element
        :param locator: elements to be checked
        :param text: text to validate
        :return:
        """
        try:
            EC.text_to_be_present_in_element(self.driver.find_element(
                *self.__get_by(locator_with_strategy=locator)), text_=text)
            return True
        except Exception as e:
            return False

    def wait_for_text_to_be_in_element(self, locator, _text, time_out=timeout):
        """
        Custom method to wait for text to be available in element
        :param locator: element to be checked
        :param _text: text to be appear in element
        :param time_out: max time out for text to appear in locator
        :return:
        """
        count = 0
        flag = False
        while count < time_out:
            count = count + 1
            if self.validate_text_in_element(locator, str(_text)) is True:
                flag = True
                break
        if not flag:
            print('Element is not loaded in DOM due to ' + str(locator))
        else:
            print('Element found!')
        return flag

    def get_random_email(self):
        num = random.choice(range(1, 99999999))
        email = "ictusharmathur" + str(num) + "@gmail.com"
        return email

    def get_locator_wrt_directory(self, locator_module, locator, pwd):
        new_locator_name = locator + pwd
        if hasattr(locator_module, new_locator_name):
            return getattr(locator_module, new_locator_name)
        elif not hasattr(locator_module, new_locator_name):
            if hasattr(locator_module, str(locator) + "_desktop_mobile"):
                return getattr(
                    locator_module,
                    str(locator) +
                    "_desktop_mobile")

    def scroll_down(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.PAGE_DOWN)
            element.send_keys(Keys.PAGE_DOWN)
        except Exception as e:
            raise e

    def scroll_up(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.PAGE_UP)
        except Exception as e:
            raise e

    def scroll_to_top(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.HOME)
        except Exception as e:
            raise e

    @staticmethod
    def scroll_to_top_android(self):
        '''
        Method to scroll to an element
        :param locator:
        :return:
        '''
        try:
            actions = TouchAction(self.driver)
            actions.press(x=18, y=1994).move_to(x=7, y=7).release().perform()
        except Exception as e:
            raise Exception("Unable to scroll due to " + str(e))

    @staticmethod
    def scroll_to_bottom(self):
        '''
        Method to scroll to an element
        :param locator:
        :return:
        '''
        try:
            actions = TouchAction(self.driver)
            actions.press(
                x=510, y=1703).move_to(
                x=375, y=450).release().perform()
        except Exception as e:
            raise Exception("Unable to scroll due to " + str(e))

    def scroll_up_index(self, locator, index, wait_time=2):
        """
        Scroll up WebPage
        :param locator: locator
        :param index: number of times up scroll
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            for i in range(index):
                element.send_keys(Keys.UP)
        except Exception as e:
            raise e

    def scroll_down_index(self, locator, index, wait_time=2):
        """
        Scroll up WebPage
        :param locator: locator
        :param index: number of times down scroll
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            for i in range(1, index):
                element.send_keys(Keys.DOWN)
        except Exception as e:
            raise e

    def fake_geolocation(self, latitude, longitude):
        """
        Method to fake geolocation
        """
        try:
            self.driver.execute_cdp_cmd(
                "Browser.grantPermissions",
                {
                    "permissions": ["geolocation"]
                }
            )
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": 100
            }
            self.driver.execute_cdp_cmd(
                "Emulation.setGeolocationOverride", params)
            return self.driver
        except Exception as e:
            raise e

    def press_down_key(self, locator, wait_time=2):
        '''
        Press the down key on the element
        '''
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
        except Exception as e:
            raise e

    def press_right_key(self, locator, wait_time=2):
        '''
        Press the right key on the element
        '''
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ARROW_RIGHT, Keys.RETURN)
        except Exception as e:
            raise e

    def press_left_key(self, locator, wait_time=2):
        '''
        Press the left key on the element
        '''
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ARROW_LEFT, Keys.RETURN)
        except Exception as e:
            raise e

    def hover(self, locator, wait_seconds=2):
        """
        Hover over the element
        :param locator: locator
        :param wait_seconds: time to wait
        :return:
        """
        element = self.find_element(locator)
        action_obj = ActionChains(self.driver)
        action_obj.move_to_element(element)
        action_obj.perform()

    def read_browser_console_log(self, log_type='browser'):
        """
        Read Browser Console log
        :param log_type: driver.get_log('browser')
            driver.get_log('driver')
            driver.get_log('client')
            driver.get_log('server')
        :return: logs
        """
        return self.driver.get_log(log_type)

    def execute_javascript(self, js_script):
        """
        Execute javascipt
        :param js_script:
        :return:
        """
        try:
            return self.driver.execute_script(js_script)
        except Exception as e:
            raise e

    def accept_alert(self):
        """
        Accepts Java Alert
        :return:
        """
        try:
            self.driver.switch_to_alert().accept()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def dismiss_alert(self):
        """
        Dismiss Java Alert
        :return:
        """
        try:
            self.driver.switch_to_alert().dismiss()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def wait_till_element_is_present(self, locator, timeout=timeout):
        """
        WebDriver Explicit wait till element is present
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=2,
                ignored_exceptions=NoSuchElementException).until(
                EC.presence_of_element_located(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_present_android(self, locator, timeout=10):
        """
        WebDriver Explicit wait till element is present
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout). \
                until(EC.presence_of_element_located(self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_visible(self, locator, timeout=timeout):
        """
        WebDriver Explicit wait till element is not visible, once visible wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """

        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                ignored_exceptions=NoSuchElementException).until(
                EC.visibility_of_element_located(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_visible_and_validate(self, locator, timeout=timeout):
        """
        WebDriver Explicit wait till element is not visible, once visible wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """

        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                ignored_exceptions=NoSuchElementException).until(
                EC.visibility_of_element_located(
                    self.__get_by(locator)))
            return True
        except Exception as e:
            return False

    def wait_till_element_is_invisible(self, locator, timeout=timeout):
        web_element = self.find_element(locator)
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=2). \
                until(
                EC.invisibility_of_element_located(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_clickable(self, locator, timeout=timeout):
        """
        WebDriver Explicit wait till element is not clickable, once clickable wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            web_element = self.find_element(locator)
            element = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=2,
                ignored_exceptions=NoSuchElementException).until(
                EC.element_to_be_clickable(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_url_contains(self, url_substring, timeout=timeout):
        """
        WebDriver Explicit wait till the current url contains a case-sensitive substring
        :param url_substring: url_substring to be checked
        :param timeout: waiting time
        :return: True when the url matches, TimeoutException otherwise
        """
        try:
            return WebDriverWait(self.driver, timeout). \
                until(EC.url_contains(url_substring))
        except Exception:
            raise TimeoutException(
                f"URL does not contain \"{url_substring}\" substring") from Exception

    def wait_till_method(self, method, timeout=timeout):
        """
        WebDriver Explicit wait till a custom method is executed.
        Use this method only after you make sure there is no any built-in method in the
        "selenium.webdriver.support.expected_conditions" module for the element you need to wait.
        :param method: method to be checked
        :param timeout: waiting time
        :return: WebElement (can also be True or False) returned by the method
        """
        try:
            return WebDriverWait(self.driver, timeout).until(method)
        except Exception as e:
            raise e

    def teardown_browser(self):
        """
        Close all browser instances
        :return:
        """
        self.driver.quit()

    def close_browser(self):
        """
        Close current browser instance
        :return:
        """
        self.driver.close()

    def disconnect_browser(self):
        """
        Disconnect browser
        :return:
        """
        self.driver.set_network_conditions(
            offline=True,
            latency=1,
            download_throughput=500 * 1024,
            upload_throughput=500 * 1024)

    def connect_browser(self):
        """
        Connect browser
        :return:
        """
        self.driver.set_network_conditions(
            offline=False,
            latency=1,
            download_throughput=500 * 1024,
            upload_throughput=500 * 1024)

    def get_network_conditions(self):
        """
        Gets Chrome network emulation settings
        :return: A dict. For example:
                {'latency': 4, 'download_throughput': 2, 'upload_throughput': 2,
                'offline': False}
        """
        return self.driver.get_network_conditions()

    def print_version(self):
        """
        Prints version
        :return:
        """
        print("print_version = 2.0")

    def maximize_browser(self):
        """
        Maximize the browser
        :return:
        """
        self.driver.maximize_window()

    def back(self):
        """
        browser back button
        :return:
        """
        self.driver.back()

    def is_element_present(self, locator):
        """
        Check the presence of element.
        :return: Boolean
        """
        try:
            self.find_element(locator)
        except BaseException:
            return False
        return True

    def get_css_value(self, locator, css_property):
        """"
        This method will get the CSS property of the element
        :return: CSS property Value

        Usage
        get_css_value(locator,"color")
        get_css_value(locator,"font-family")
        get_css_value(locator,"font-size")
        The above code will return value in RGB format such as “rgba(36, 93, 193, 1)”
        """
        element = self.find_element(locator)
        return element.value_of_css_property(css_property)

    def get_current_window_handle(self):
        """
        Returns the handle of the current window.
        :return: string containing current window handle
        """
        return self.driver.current_window_handle

    def switch_control_to_app(self):
        '''
        Method to switch control to app
        '''
        try:
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            raise Exception("Unable to switch control to app")

    def hide_keyboard(self):
        pass

    def switch_control_to_webview(self):
        '''
        Method to switch control to app
        '''
        try:
            webview = self.driver.contexts[1]
            self.driver.switch_to.context(webview)
        except Exception as e:
            raise Exception(
                "Unable to switch control to webview due to " + str(e))

    def handle_pop_up(self, btn_to_click):
        """
        Method to handle (accept/reject) pop ups
        :param btn_to_click: text of the button to be clicked, e.g. "Allow", "Block"
        :return:
        """
        try:
            self.switch_control_to_app()
            self.driver.find_element_by_xpath(
                f".//*[@text='{btn_to_click}']").click()
            self.switch_control_to_webview()
        except Exception as e:
            raise Exception("Unable to handle the pop up due to " + str(e))

    def get_window_handles(self):
        """
        Returns the list containing handles of all windows within the current session.
        :return: list containing all opened window handles in current session
        """
        return self.driver.window_handles

    def is_special_char_available(self, url):

        url = unquote(url)
        allowed_ascii = range(128)
        try:
            for literal in url:
                try:
                    if not ord(literal) in allowed_ascii:
                        return True
                except TypeError as e:
                    raise TypeError(str(e), url, literal)
            return False
        except Exception as e:
            raise Exception("Unable to check special character: " + str(e))

    def switch_to_new_window(self, win_handle):
        """
        Switch to window corresponding to windows handle id
        :return:
        """
        self.driver.switch_to.window(win_handle)

    def refresh_browser(self):
        """
        Refreshes the page
        :return:
        """
        self.driver.refresh()

    def handle_pop_up(self, btn_to_click):
        """
        Method to handle (accept/reject) pop ups
        :param btn_to_click: text of the button to be clicked, e.g. "Allow", "Block"
        :return:
        """
        try:
            self.driver.find_element_by_xpath(
                f".//*[@text='{btn_to_click}']").click()
        except Exception as e:
            raise Exception("Unable to handle the pop up due to " + str(e))

    def get_size(self, file):
        """
        Function to check the size of the file
        :return:
        """
        try:
            file_size = os.path.getsize(
                f"C:\\Users\\{os.environ['USERNAME']}\\Downloads\\" + str(file))
            return file_size
        except Exception as e:
            raise Exception("Unable to get file size: " + str(e))

    def remove_file(self, file):
        """
        Function to remove the file from location
        :param file:
        :return:
        """
        if file:
            os.remove(
                f"C:\\Users\\{os.environ['USERNAME']}\\Downloads\\" +
                str(file))

    def get_full_page_screen_shot(self, filename):
        self.driver.save_screenshot(filename)

    def get_page_cookies(self):
        return self.driver.get_cookies()

    def get_page_useragent(self):
        return self.driver.execute_script("return navigator.userAgent")

    def get_console_error_logs(self, driver_obj):
        return driver_obj.get_log('browser')


class Strategy(Enum):
    """
    Locator Strategy Constants
    """
    XPATH = "xpath"
    ID = "id"
    CSS = "css"
    TAGNAME = "tag name"
