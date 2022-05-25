import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from allure_commons.types import AttachmentType
from Web.WebConstants.loginPageConst import LoginPageConst

@allure.title("Login Page Steps")
class LoginPage(LoginPageConst):
    def __init__(self,driver:WebDriver):
        self.driver = driver
    @allure.step('Landing On Login Page')
    def landOnLoginPage(self):
        driver = self.driver
        driver.get(self.login_page_url)

    @allure.step('Enter an email')
    def enterEmail(self,email):
        driver = self.driver
        email_field = driver.find_element(By.XPATH,self.login_email_field_Xpath)
        email_field.send_keys(email)
        print(email_field.get_attribute('value'))
        print(email)
        try:
            assert email_field.get_attribute('value') == email
        except AssertionError:
            print('The email is not in the field')
            allure.attach(self.driver.get_screenshot_as_png(),
                              name='LoginPageEmailErr',
                              attachment_type=AttachmentType.PNG)

    @allure.step('Enter a password')
    def enterPassword(self,password):
        driver = self.driver
        password_field = driver.find_element(By.XPATH,self.login_password_field_Xpath)
        password_field.send_keys(password)
        print(password_field.get_attribute('value'))
        print(password)
        try:
            assert password_field.get_attribute('value') == password
        except AssertionError:
                print('The password is not in the field')
                allure.attach(self.driver.get_screenshot_as_png(),
                              name='LoginPagePasswordErr',
                              attachment_type=AttachmentType.PNG)

    @allure.step('Clicking on send button')
    def clickOnLoginBtn(self):
        driver = self.driver
        send_btn = driver.find_element(By.XPATH,self.login_send_button_Xpath)
        send_btn.click()
        # WebDriverWait(driver,10).until(
        #     EC.visibility_of(
        #         driver.switch_to.alert
        #     )
        # )

    @allure.step('Clicking on the pop-up message')
    def clickOnPopUpMsg(self,msg):
        driver = self.driver
        alert = driver.switch_to.alert
        alert_msg = alert.text
        print(alert_msg)
        try:
            assert alert_msg == msg
        except AssertionError:
            print(f"The {alert_msg} is the wrong message!")
        print("Alert shows following message: " + alert_msg)
        alert.accept()
        print(" Clicked on the OK Button in the Alert Window")



