import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
from data.onboarding_texts import ONBOARDING_TEXTS
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        action="store",
        default="local_emulator",
        choices=["local_emulator", "local_real", "bstack"],
        help="Test context: local_emulator, local_real, bstack",
    )


@pytest.fixture(scope="session")
def config(request):
    context = request.config.getoption("--context")
    return Config(context)


@pytest.fixture(scope="function", autouse=True)
def mobile_management(config):
    options = UiAutomator2Options()

    options.platform_name = config.platform_name
    options.automation_name = config.automation_name
    options.device_name = config.device_name
    options.no_reset = config.no_reset
    options.full_reset = config.full_reset
    options.language = config.language
    options.locale = config.locale

    options.set_capability("appium:ignoreHiddenApiPolicyError", True)
    options.set_capability("appium:skipDeviceInitialization", True)

    if config.udid:
        options.udid = config.udid

    if config.platform_version:
        options.platform_version = config.platform_version

    if config.app_path:
        options.app = config.app_path

    if config.app_package:
        options.app_package = config.app_package

    if config.app_activity:
        options.app_activity = config.app_activity

    if config.context == "bstack":
        options.set_capability(
            "bstack:options",
            {
                "userName": config.bstack_user_name,
                "accessKey": config.bstack_access_key,
                "projectName": "Wikipedia mobile tests",
                "buildName": "wikipedia-onboarding-build",
                "sessionName": "Wikipedia onboarding",
            },
        )

    driver = webdriver.Remote(
        command_executor=config.remote_url,
        options=options,
    )

    browser.config.driver = driver
    browser.config.timeout = 10

    try:
        yield
    finally:
        if config.app_package:
            try:
                driver.terminate_app(config.app_package)
            finally:
                driver.quit()

@pytest.fixture
def onboarding_texts(config):
    return ONBOARDING_TEXTS[config.language]