from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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
el = driver.find_element(AppiumBy.XPATH, '//*[@text="CONTACT US FORM"]')

el.click()