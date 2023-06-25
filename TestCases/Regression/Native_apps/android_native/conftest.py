from NativePageObjects.HomePage import NativeHomePage
from NativePageObjects.FooterPage import NativefooterPage
import pytest
from Utilities.Webdriver import GetWebdriver
import allure


@pytest.fixture(scope='class')
def platform(request):
    """pytest fixture for platform"""
    return request.config.getoption("-P")


@pytest.fixture(scope='class')
def os_version(request):
    """pytest fixture for os version"""
    return request.config.getoption("-O")


@pytest.fixture(scope='class')
def headless(request):
    """pytest fixture for headless browsing"""
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
def create_resource(request, os_version, headless, latitude, longitude, platform, app_path):
    teardown_flag = False
    driver = GetWebdriver.get_android_driver(app_path=app_path)
    home_obj = NativeHomePage(driver)
    footer_obj = NativefooterPage(driver)
    request.cls.home_obj = home_obj
    request.cls.footer_obj = footer_obj
    request.cls.latitude = latitude
    request.cls.longitude = longitude
    request.cls.driver = driver
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
