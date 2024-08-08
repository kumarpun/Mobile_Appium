from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '15',
    'deviceName': 'sdk_gphone64_arm64',
    'app': '/Users/tekkon/Downloads/Android_Demo_App.apk'
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CONTACT US FORM")')
# el = driver.find_element(AppiumBy.XPATH, '//*[@text="CONTACT US FORM"]')


wait = WebDriverWait(driver,5,poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

ele = wait.until(lambda x:x.find_element(AppiumBy.XPATH, '//*[@text="CONTACT US FORM"]'))
ele.click()

# print("package:", driver.current_package)
# print("activity:", driver.current_activity)
