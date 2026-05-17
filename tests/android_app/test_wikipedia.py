import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


ONBOARDING_TITLE = (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
FORWARD_BUTTON = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
DONE_BUTTON = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")


@allure.title("Проверка onboarding-экранов Wikipedia")
def test_wikipedia_onboarding(onboarding_texts):
    with allure.step("Проверить первый onboarding screen"):
        browser.element(ONBOARDING_TITLE).should(be.visible)
        browser.element(ONBOARDING_TITLE).should(have.text(onboarding_texts["screen_1"]))

    with allure.step("Перейти на второй onboarding screen"):
        browser.element(FORWARD_BUTTON).click()

    with allure.step("Проверить второй onboarding screen"):
        browser.element(ONBOARDING_TITLE).should(be.visible)
        browser.element(ONBOARDING_TITLE).should(have.text(onboarding_texts["screen_2"]))

    with allure.step("Перейти на третий onboarding screen"):
        browser.element(FORWARD_BUTTON).click()

    with allure.step("Проверить третий onboarding screen"):
        browser.element(ONBOARDING_TITLE).should(be.visible)
        browser.element(ONBOARDING_TITLE).should(have.text(onboarding_texts["screen_3"]))

    with allure.step("Перейти на четвертый onboarding screen"):
        browser.element(FORWARD_BUTTON).click()

    with allure.step("Проверить четвертый onboarding screen"):
        browser.element(ONBOARDING_TITLE).should(be.visible)
        browser.element(ONBOARDING_TITLE).should(have.text(onboarding_texts["screen_4"]))

    with allure.step("Завершить onboarding"):
        browser.element(DONE_BUTTON).click()