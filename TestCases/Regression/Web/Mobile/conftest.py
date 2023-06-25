import os

from WebPageObjects.Home_Page import HomePage
from WebPageObjects.Footer_Page import FooterPage
from WebPageObjects.SignUp_Page import SignUpPage
import pytest
from Utilities import PageBase
import time
import Static.Constants as const
from Utilities.Webdriver import GetWebdriver
import allure


@pytest.fixture(scope='class')
def browser(request):
    "pytest fixture for browser"
    return request.config.getoption("-B")


@pytest.fixture(scope='class')
def browserstack_flag(request):
    "pytest fixture for browserstack flag"
    return request.config.getoption("-M")


@pytest.fixture(scope='class')
def platform(request):
    "pytest fixture for platform"
    return request.config.getoption("-P")


@pytest.fixture(scope='class')
def os_version(request):
    "pytest fixture for os version"
    return request.config.getoption("-O")


@pytest.fixture(scope='class')
def ic_server(request):
    "pytest fixture for ic server"
    return request.config.getoption("-S")


@pytest.fixture(scope='class')
def url(request):
    "pytest fixture for url"
    return request.config.getoption("-U")


@pytest.fixture(scope='class')
def headless(request):
    "pytest fixture for headless browsing"
    return request.config.getoption("-H")


@pytest.fixture(scope='class')
def latitude(request):
    """
    Pytest fixture for passing latitude coordinates
    """
    return request.config.getoption("--lat")


@pytest.fixture(scope='class')
def longitude(request):
    """
    Pytest fixture for passing longitude coordinates
    """
    return request.config.getoption("--long")


@pytest.fixture(scope='function')
def create_resource(request, browser, ic_server, os_version,
                    url, headless, latitude, longitude, platform):
    global driver, home_obj, footer_obj
    variable = os.path.dirname(os.path.abspath(__file__))
    cwd = os.path.split(str(variable))[-1].lower()
    cwd = "_" + cwd
    teardown_flag = False
    request.cls.server = ic_server
    driver = GetWebdriver.get_webdriver(browser, os_version, headless)
    driver.set_window_size(400, 613)
    home_obj = HomePage(driver, cwd)
    sign_up_obj = SignUpPage(driver, cwd)
    footer_obj = FooterPage(driver, cwd)
    if url:
        page = url
        driver.get(page)
    else:
        page = f"https://{request.cls.server}.insomniacookies.com"
        driver.get(page)
    request.cls.home_obj = home_obj
    request.cls.footer_obj = footer_obj
    request.cls.sign_up_obj = sign_up_obj
    request.cls.latitude = latitude
    request.cls.longitude = longitude
    request.cls.driver = driver
    request.cls.cwd = cwd
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        teardown_flag = True
        allure.attach(driver.get_screenshot_as_png())
        name = request.node.name
        home_obj.get_full_page_screen_shot(
            '../screenshots' + '/' + name + ".png")
        home_obj.teardown_browser()
    if not teardown_flag:
        home_obj.teardown_browser()


@pytest.fixture(scope='function')
def login(request):
    home_obj = HomePage(request.cls.driver, request.cls.cwd)
    login_obj = home_obj.click_header_login()
    login_obj.enter_username(const.uname)
    login_obj.enter_password(const.password)
    login_obj.click_login()
    home_obj.is_user_logged_in()


@pytest.fixture(scope='function')
def login_to_edit(request):
    home_obj = HomePage(request.cls.driver, request.cls.cwd)
    login_obj = home_obj.click_header_login()
    login_obj.enter_username(const.uname2)
    login_obj.enter_password(const.password2)
    login_obj.click_login()
    home_obj.is_user_logged_in()


@pytest.fixture(scope='function')
def set_browser_resolution_for_mobile(request):
    """
    Set browser window for mobile resolution
    """
    return request.cls.driver.set_window_size(398, 680)
