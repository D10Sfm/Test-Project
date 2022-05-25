import allure
import pytest
from Web.Base.Chrome.driverChrome import DriverChrome
from Web.Pages.loginPage import LoginPage
from Web.WebConstants.loginPageConst import LoginPageConst


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('setup_chrome')
class TestLoginPage(DriverChrome,LoginPageConst):
    @pytest.mark.sanity
    def test_login_valid(self,setup_chrome):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.landOnLoginPage()
        loginPage.enterEmail(self.user_details['email'])
        loginPage.enterPassword(self.user_details['password'])
        loginPage.clickOnLoginBtn()
        loginPage.clickOnPopUpMsg('sss')


