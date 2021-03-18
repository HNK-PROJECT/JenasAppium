import allure
import pytest
from mobile import JeansApp


# pytest --alluredir allure_results  -v test_app.py

@allure.feature('Full visit test')
@allure.story('Тестирование синхронизации, визита и заказа в визите')
@allure.severity('blocker')
def test_full_visit(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.visit_start()
    ma.visit_start()
    ma.visit_finish()
    ma.sync()
