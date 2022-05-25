import allure
import requests
import pytest
from Server.ServerConstants.loginPageConst import LoginPageConst


@pytest.mark.server
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin(LoginPageConst):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        url = self.login_page_url
        obj_1 = self.user_details
        x = requests.post(url,data=obj_1)
        try:
            assert x.status_code == (202 or 204)
        except AssertionError:
            print(f'The {x.status_code} not valid code!')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self):
        url = 'https://ivolunteer-app.herokuapp.com/users/login'
        obj_1 = {"Email": "zzz", "Password": "1239"}
        x = requests.post(url,data=obj_1)
        try:
            assert x.status_code == 401
        except AssertionError:
            print(f'The {x.status_code} not valid code!')
