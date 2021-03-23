import pytest
from appium import webdriver

class Base:
    def __init__(self, driver):
        desired_capabilities = {
            "app": "/Users/annakostromina/JeansMobileApplication/JeansMobileApplication/bin/iPhoneSimulator/Debug/JeansMobileApplication.app",
            "platformName": "iOS",
            "platformVersion": "14.4",
            "deviceName": "iPhone 8"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

