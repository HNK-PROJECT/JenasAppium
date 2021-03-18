import time
import allure
from selenium.webdriver.common.by import By
from base_page import Base
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from allure_commons.types import AttachmentType


class JeansApp(Base):

    def auth(self):
        allow_check = self.driver.find_element(By.NAME, 'Allow While Using App')
        allow_check.click()
        authorize = self.driver.find_element(By.NAME, 'Images/Menu/ServiceButton.png').click()
        authorize = self.driver.find_element(By.NAME, 'Авторизация').click()
        authorize = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeTextField[`value == "dobra01"`]').clear()
        authorize = self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeTextField"').send_keys("nursr1")
        authorize = self.driver.find_element(By.NAME, 'Войти').click()
        authorize = self.driver.find_element(By.NAME, 'Да').click()
        time.sleep(40)
        with allure.step('Фиксируем авторизацию и синхру'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def visit_window(self):
        visit_module = self.driver.find_element(By.NAME, 'Images/Menu/VisitsButton.png').click()
        visit_module = self.driver.find_element(By.NAME, 'Внеплановые').click()
        visit_module = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther').send_keys("kim")
        TouchAction(self.driver).tap(None, 340, 125, 1).perform()
        with allure.step('Фиксируем список визитов'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def visit_start(self):
        visit = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther').click()
        TouchAction(self.driver).tap(None, 180, 630, 1).perform()

    def visit_order(self):
        visit_order = self.driver.find_element(By.NAME,'Меню').click()
        visit_order = self.driver.find_element(By.NAME,'Заказ').click()
        TouchAction(self.driver).tap(None, 187, 590, 1).perform()
        visit_order = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]').send_keys("22")
        visit_order = self.driver.find_element(By.NAME,'< Назад').click()
        with allure.step('Фиксируем формироваие заказа'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def visit_finish(self):
        visit_finish = self.driver.find_element(By.NAME,'Меню').click()
        visit_finish = self.driver.find_element(By.NAME,'Завершение').click()
        visit_finish = self.driver.find_element_by_ios_predicate('label == "Сохранить"').click()
        visit_finish = self.driver.find_element_by_ios_predicate('label == "Закрыть"').click()
        time.sleep(10)
        with allure.step('Фиксируем завршение визита'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        TouchAction(self.driver).tap(None, 180, 630, 1).perform()
        time.sleep(5)

    def sync(self):
        visit_finish = self.driver.find_element('Images/Menu/SynchronizationButton.png').click()
        time.sleep(10)



