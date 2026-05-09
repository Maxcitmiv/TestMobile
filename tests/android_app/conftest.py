import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def mobile_management():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Samsung Galaxy S22 Ultra"
    options.platform_version = "12.0"
    options.app = "bs://sample.app"

    options.set_capability(
        "bstack:options",
        {
            "userName": "maximshkolnyy_wJ1Pfe",
            "accessKey": "e1Nv2ynudY3gSpmdsJN8",
            "projectName": "BrowserStack Sample",
            "buildName": "browserstack-build-1",
            "sessionName": "Android test",
            "local": "false",
            "selfHeal": "true",
            "aiAuthoring": "true",
        },
    )

    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.timeout = 10

    yield

    browser.quit()