import pytest
from selenium import webdriver



class DriverChrome:

    @pytest.fixture(autouse=True)
    def setup_chrome(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield self.driver
        print("-----------------------------------------")
        print("Tests is finished")
        self.driver.close()
        self.driver.quit()
