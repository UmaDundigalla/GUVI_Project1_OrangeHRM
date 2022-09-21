import time
from selenium.webdriver.common.by import By



class Admin_AddNewUser:

    admin_menu_linktxt = 'Admin'
    btn_add_admin_path = "//button[normalize-space()='Add']"
    btn_userrole_path = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']" \
                                   "//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]"
    user_role_admin_xpath = "//*[contains(text(),'Admin')]"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    click_emp_name = "//*[contains(text(),'Steve')]"
    btn_status_dropdown_xpath = "//div[3]/div/div[2]/div/div/div[@class='oxd-select-text-input']"
    status_enabled_xpath = "//*[contains(text(),'Enabled')]"
    username_xpath = "//div[1]//div[4]//input"
    password_path = "//div[1]/div/div[2]/input"
    confirm_password_xpath = "//div[2]/div/div[2]/input"
    save_admin_xpath = "//button[normalize-space()='Save']"


#Search User in Admin
    username1_path = "//form/div[1]/div//div[2]/input"
    btn_search_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

#Verify User
    name_search = "//div[@class='oxd-table-card']//div//div[2]"


#Logout from Application
    click_profile = "//i/preceding::p"
    logout_xpath = "//a[text()='Logout']"

#Login Again with Newly Created user details
    txtbx1_email_xpath = "//input[@placeholder='Username']"
    txtbx1_password_xpath = "//input[@placeholder='Password']"
    btn1_login_button = "//button[normalize-space()='Login']"


    def __init__(self,driver):
        self.driver = driver

    def Admin_add(self,username1, password1, confirmpassword, employeename):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,self.admin_menu_linktxt).click()
        self.driver.find_element(By.XPATH,self.btn_add_admin_path).click()
        self.driver.find_element(By.XPATH,self.btn_userrole_path).click()
        self.driver.find_element(By.XPATH,self.user_role_admin_xpath).click()
        self.driver.find_element(By.XPATH,self.employee_name_xpath).send_keys(employeename)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.click_emp_name).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.btn_status_dropdown_xpath).click()
        self.driver.find_element(By.XPATH,self.status_enabled_xpath).click()
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username1)
        self.driver.find_element(By.XPATH,self.password_path).send_keys(password1)
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirmpassword)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.save_admin_xpath).click()

    def search_user_name(self, Username):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.username1_path).send_keys(Username)
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def check_customer_added(self):
        return self.driver.find_element(By.XPATH, self.name_search).text

    def logout(self):
        self.driver.find_element(By.XPATH, self.click_profile).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        time.sleep(5)

    def Again_login(self, username1, password1):
        self.driver.find_element(By.XPATH, self.txtbx1_email_xpath).send_keys(username1)
        self.driver.find_element(By.XPATH, self.txtbx1_password_xpath).send_keys(password1)
        self.driver.find_element(By.XPATH, self.btn1_login_button).click()