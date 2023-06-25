import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GetWebdriver:
    @staticmethod
    def get_webdriver(browser, os_version, headless=False):
        if browser.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--privileged")
            if headless == "True":
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=3840,2160")
                chrome_options.add_argument("--disable-gpu")
            prefs = {'safebrowsing.enabled': 'false',
                     'profile.default_content_setting_values.geolocation': 2}
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
            chrome_options.add_experimental_option("prefs", prefs)

            if os.environ.get('localIP'):
                hub = "http://%s/wd/hub" % os.environ.get("localIP")
                return webdriver.Remote(
                    command_executor=hub,
                    options=chrome_options,
                    desired_capabilities=desired_capabilities)
            elif os_version == "Linux":
                return webdriver.Chrome(
                    'chromedriver',
                    options=chrome_options,
                    desired_capabilities=desired_capabilities)
            elif os_version == "Mac":
                return webdriver.Chrome(
                    os.path.join(
                        os.path.abspath(
                            __file__ + "/../../"),
                        "Webdriver/chromedriver_mac/chromedriver"),
                    options=chrome_options,
                    desired_capabilities=desired_capabilities)
            elif os_version == "Windows":
                return webdriver.Chrome(
                    os.path.join(
                        os.path.abspath(
                            __file__ + "/../../"),
                        "Webdriver\\chromedriver_windows\\chromedriver.exe"),
                    options=chrome_options,
                    desired_capabilities=desired_capabilities)

    @staticmethod
    def get_android_driver(app_path):
        desired_caps_android = dict()
        desired_caps_android['platformName'] = 'Android'
        desired_caps_android['platformVersion'] = '10.0'
        desired_caps_android['deviceName'] = 'emulator-5554'
        desired_caps_android['app'] = str(app_path)
        desired_caps_android['appPackage'] = "com.insomniacookies.insomnia"
        desired_caps_android['autoAcceptAlerts'] = True
        desired_caps_android['autoGrantPermissions'] = True
        desired_caps_android['uiautomator2ServerInstallTimeout'] = 60000
        desired_caps_android['uiautomator2ServerLaunchTimeout'] = 60000
        desired_caps_android['avdArgs'] = "-no-window"
        return webdriver.Remote(
            "http://0.0.0.0:4723/wd/hub",
            desired_caps_android)

    @staticmethod
    def get_ios_driver():
        desired_caps_ios = dict()
        desired_caps_ios['platformName'] = 'iOS'
        desired_caps_ios['platformVersion'] = '14.0'
        desired_caps_ios['deviceName'] = 'iPhone 11'
        desired_caps_ios['bundleId'] = 'com.insomniacookies.insomnia'
        desired_caps_ios['automationName'] = 'XCUITest'
        desired_caps_ios['locationServicesEnabled'] = False
        return webdriver.Remote("http://0.0.0.0:4725/wd/hub", desired_caps_ios)
