import pytest
import time


from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login_Page
from PageObjects.PIM import CreateNewEmployee
from PageObjects.AdminPage import Admin_AddNewUser
from TestCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_AddNewUser:

    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    employeename = ReadConfig.getEmployeeName()
    username1 = ReadConfig.getUserName1()
    password1 = ReadConfig.getPassword1()
    confirmpassword = ReadConfig.getPassword1()

    logger = LogGen.loggen()

    def test_add_user(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login_Page(self.driver)
        self.driver.implicitly_wait(10)
        lp = Login_Page(self.driver)
        self.driver.implicitly_wait(10)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        self.logger.info("******Logged in Successfully******")

        self.logger.info("*******tc003_Admin-AddNewUser")
        adduser = Admin_AddNewUser(self.driver)


        adduser.Admin_add(self.username1, self.password1, self.confirmpassword, self.employeename)
        self.logger.info("******Added New User******")
        self.logger.info("*******tc003_Admin-AddNewUser Ending")

# Verify_User in Admin and Logout from Application:
        search_user = Admin_AddNewUser(self.driver)
        self.logger.info("*******tc004_Verify-NewUser")
        search_user.search_user_name(self.username1)
        username = search_user.check_customer_added()
        print(username)
        if username == ReadConfig.getUserName1():
            self.logger.info("*******the username is found*******")
            print("*********User is Successfully Added*******")
        else:
            self.logger.info("********the username is not found*******")
        logout = Admin_AddNewUser(self.driver)
        logout.logout()

        self.logger.info("******Ending tc004_Verify-NewUser******")

# Login using Newly Created Username
    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*******tc005_Login_NewUser*******")
        self.logger.info("******Login with New User details********")
        login = Admin_AddNewUser(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        login.Again_login(self.username1, self.password1)
        act_url = self.driver.current_url
        if act_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
            self.logger.info("******Login is Successful")
            assert True
        else:
            self.driver.save_screenshot("C:\\UmaRaniDundigalla\\UmaRani_workspace\\GUVI"
                                        "\\GUVI_Project1\\ScreenShots" + "tc001_LoginFailed")
            self.logger.info("******Login Failed******")
        self.logger.info("******Ending tc005_Login_NewUser********")
