import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver():
    desired_capabilities = {
      "app": "/Users/annakostromina/JeansMobileApplication/JeansMobileApplication/bin/iPhoneSimulator/Debug/JeansMobileApplication.app",
      "platformName": "iOS",
      "platformVersion": "14.4",
      "deviceName": "iPhone 8"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
