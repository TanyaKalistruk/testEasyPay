import allure

from src.PageObjects.api_page import Api
from src.credentials import PASSWORD, MANAGER_EMAIL
from src.db_conn import DBConnection


url_update_price = 'http://localhost:8080/manager/utility/price/add'
url_delete_inspector = 'http://localhost:8080/manager/schedule/deleteInspector'
url_add_inspector = 'http://localhost:8080/manager/schedule/addInspector'


def test_change_price():
    cookie_login = Api.login_api(MANAGER_EMAIL, PASSWORD)
    params = {"price": '30'}
    request = Api.put_params(params, url_update_price, cookies=cookie_login)
    with allure.step('It is valid price'):
        assert request.status_code == 200


def test_delete_inspector():
    with DBConnection() as db:
        if db.check_delete_inspector() != 0:
            cookie_login = Api.login_api(MANAGER_EMAIL, PASSWORD)
            params = "109"
            request = Api.delete_params(params, url_delete_inspector, cookies=cookie_login)
            with allure.step('It is valid id for inspector'):
                assert request.status_code == 200


def test_add_inspector():
    with DBConnection() as db:
        if db.check_delete_inspector() == 0:
            cookie_login = Api.login_api(MANAGER_EMAIL, PASSWORD)
            params = "109"
            request = Api.put_params(params, url_add_inspector, cookies=cookie_login)
            with allure.step('It is valid id for inspector'):
                assert request.status_code == 200
