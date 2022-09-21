import random
import string
import time
from selenium.webdriver.common.by import By

class CreateNewEmployee:
#pim list

    btn_add_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    txt_firstname_name = "firstName"
    txt_middlename_name = "middleName"
    txt_lastname_name = "lastName"
    txt_employeeid_xpath = "//div[@class = 'oxd-grid-2 orangehrm-full-width-grid']" \
                           "//input[@class ='oxd-input oxd-input--active']"
    btn_addimg_xpath = "//button[@class='oxd-icon-button employee-image-action']"
    btn_save_xpath = "//form/div[2]//button[@type='submit']"





    def __init__(self,driver):
        self.driver = driver

#### Navigating to PIM and Creating New Employee######
    def pim(self, firstname, lastname):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
