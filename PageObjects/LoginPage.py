from selenium.webdriver.common.by import By

class Login_Page:
    txtbx_username_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

#loginpage module#
    def set_username(self, username):
        self.driver.find_element(By.XPATH,self.txtbx_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbx_username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.txtbx_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbx_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
