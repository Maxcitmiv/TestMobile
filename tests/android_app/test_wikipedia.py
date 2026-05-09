from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_search():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

@allure.title('Тест-клик')
def test_click():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Xiaomi')
    results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    results.should(have.size_greater_than(0))
    results.first.should(have.text('Xiaomi'))
    browser.element((
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector()'
        '.resourceId("org.wikipedia.alpha:id/page_list_item_title")'
        '.text("Xiaomi")'
)).click()
    
