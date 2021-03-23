import allure
import pytest
from mobile import JeansApp


# pytest --alluredir allure_results  -v test_app.py

@allure.feature('Full visit test')
@allure.story('Тестирование синхронизации, визита и заказа в визите')
@allure.severity('blocker')
def test_visit(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.visit_window()
    ma.visit_start()
    ma.visit_finish()
    ma.sync()


def test_order_and_return(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.do_order()
    ma.do_return()
    ma.ord_ret_finish()
    ma.sync()


def test_history(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.open_history()