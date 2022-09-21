import time
import string
import random
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_login:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("******Opening OrangeHRM Website******")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("*****TC001_Login*****")
        self.logger.info("******Verifying the functionality of Login******")
        lp = Login_Page(self.driver)
        self.driver.implicitly_wait(10)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        act_url = self.driver.current_url
        if act_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
            self.logger.info("******Login is Successful*******")
            assert True
        else:
            self.driver.save_screenshot("C:\\UmaRaniDundigalla\\UmaRani_workspace\\GUVI\\GUVI@OrangeHRM_Project_1\\ScreenShots" + "Test_001_LoginFailed.png")
            self.logger.info("******Login Failed******")
