import pytest


@pytest.fixture(scope='class')
def browser(request):
    """pytest fixture for browser"""
    return request.config.getoption("-B")


@pytest.fixture(scope='class')
def browserstack_flag(request):
    """pytest fixture for browserstack flag"""
    return request.config.getoption("-M")


@pytest.fixture(scope='class')
def platform(request):
    """pytest fixture for platform"""
    return request.config.getoption("-P")


@pytest.fixture(scope='class')
def os_version(request):
    """pytest fixture for os version"""
    return request.config.getoption("-O")


@pytest.fixture(scope='class')
def ic_server(request):
    """pytest fixture for ic server"""
    return request.config.getoption("-S")


@pytest.fixture(scope='class')
def url(request):
    """pytest fixture for url"""
    return request.config.getoption("-U")


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


@pytest.fixture(scope='class')
def app_path(request):
    """
    Pytest fixture for passing app path
    """
    return request.config.getoption("--app_path")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Valid options are firefox, ie and chrome")
    parser.addoption("-P", "--platform",
                     dest="platform",
                     help="The operating system: Windows 7, Linux"
                     )
    parser.addoption("-A", "--app_path",
                     dest="app_path",
                     help="App Path: ./app-dev.apk"
                     )
    parser.addoption("-O", "--os_version",
                     dest="os_version",
                     help="The operating system: xp, 7")
    parser.addoption("-S", "--ic_server",
                     dest="ic_server",
                     help="The IC Server: www,stage",
                     default="web.stage")
    parser.addoption("-U", "--url",
                     dest="url",
                     help="The URL on which tests are to be executed")
    parser.addoption("-H", "--headless",
                     dest="headless",
                     help="The mode in which Testcases are to be executed",
                     default=False)
    parser.addoption("--lat",
                     dest="latitude",
                     default="40.72975",
                     help="The latitude coordinates for faking geolocation",
                     )
    parser.addoption("--long",
                     dest="longitude",
                     default="-74.000583",
                     help="The longitude coordinates for faking geolocation")
