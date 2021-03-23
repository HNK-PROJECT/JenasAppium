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


@allure.feature('Create order and return out of visit')
@allure.story('Создание заказа и возврата вне визита')
@allure.severity('blocker')
def test_order_and_return(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.do_order()
    ma.do_return()
    ma.ord_ret_finish()
    ma.sync()


@allure.feature('Replica test')
@allure.story('Проверка заказа и возврата в модуле История')
@allure.severity('blocker')
def test_history(driver):
    ma = JeansApp(driver)
    ma.auth()
    ma.open_history()
