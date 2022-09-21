import time
from selenium.webdriver.common.by import By


class NewEmployee_Personal_Detail:
    # pim personal detail locators
    txt_nickname_xpath = "//form[@class='oxd-form']/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_other_id_xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    txt_license_no_path = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    txt_issued_date =  "//form/div[2]//div[2]//div[2]//input[@placeholder='yyyy-mm-dd']"
    txt_expiry_date_xpath = "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    txt_ssn_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    txt_sin_xpath = "//div[3]/div[2]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    txt_date_of_birth = "//form/div[3]/div[2]//div/input[@placeholder='yyyy-mm-dd']"
    btn_gender_xpath = "//label[normalize-space()='Female']"
    btn_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    btn_nationality_click = "//*[contains(text(),'Indian')]"
    btn_married_status = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_married_status_click = "//*[contains(text(),'Single')]"
    txt_military_service_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    btn_save_xpath = "//div[5]/button[@type='submit']"
    btn_blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text oxd-select-text--active']"
    btn_blood_group = "//*[contains(text(),'O+')]"
    btn_save1_xpath = "//form/div[2]/button[@type='submit']"

    # contact details
    link_contact_linktxt = "Contact Details"
    txt_street1_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_street2_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_city_xpath = "//form[@class='oxd-form']/div[1]//div[3]//div[2]/input"
    txt_state_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//input"
    txt_pincode_xpath = "//form[@class='oxd-form']//div[1]//div[5]//div[2]/input"
    btn_country_path_select = "//*[contains(text(),'-- Select --')]"
    btn_country_click_xpath = "//*[text()='India']"
    txt_homenumber_xpath = "//form[@class='oxd-form']/div[2]//div[1]/div/div[2]/input"
    txt_mobile_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_work_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_workemail_xpath = "//form[@class='oxd-form']/div[3]/div/div[1]//input"
    txt_othermail_xpath = "//form[@class='oxd-form']/div[3]/div/div[2]//input"
    txt_contactsave_xpath = "//form[@class='oxd-form']/div[4]//button"

    # emergency details locators
    link_emergency_linktxt = "Emergency Contacts"
    btn_add_contact = "//div/div[2]/div[1]/div/button"
    txt_name_xpath = "//form/div[1]/div/div[1]//input"
    txt_relationship_xpath = "//form/div[1]/div/div[2]//input"
    txt_mobileno_xpath = "//form/div[2]/div/div[2]//input"
    txt_workno_xpath = "//form/div[2]/div/div[3]//input"
    btn_emergencycontactsave_xpath = "//form[@class='oxd-form']/div//button[2]"

    # dependent locators
    link_dependent_linktxt = "Dependents"
    btn_add_dependent = "//div[2]/div//div[2]/div[1]//button"
    txt_dependentname_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    btn_relation_xpath = "//form/div//div[2]//div[2]/div"
    btn_relation_click_xpath = "//*[contains(text(),'Child')]"
    txt_add_dob_xpath = "//form[@class='oxd-form']/div[2]//input"
    btn_dependentsave_xpath = "//button[@type='submit']"

    # Immigration
    link_immigration_linktxt = "Immigration"
    btn_add_immigration = "//div[2]/div[1]/div/button[@class='oxd-button oxd-button--medium oxd-button--text']"
    txt_number_xpath = "//form/div[2]/div/div[1]//input"
    txt_issueddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_expirydate_xpath = "//div[3]//div[2]//input[@placeholder='yyyy-mm-dd']"
    txt_eligible_status_xpath = "//form[@class='oxd-form']/div[2]//div[4]//input"
    btn_issuedby_xpath = "//div[contains(text(),'-- Select --')]"
    btn_issuedby_click_xpath = "//*[contains(text(),'India')]"
    txt_eligiblereview_xpath = "//form[@class='oxd-form']/div[2]/div/div[6]//input"
    command_xpath = "//textarea[@placeholder='Type Comments here']"
    btn_saveimmigration_xpath = "//form/div[3]/button[2]"

    # job
    link_job_linktext = "Job"
    txt_joineddate_xpath = "//div[@class='oxd-date-input']/input"
    btn_drp_job_title_xpath = "//form[@class='oxd-form']/div/div/div[2]//i"
    btn_select_job_title = "//*[contains(text(),'Chief Financial Officer')]"
    btn_drp_job_category = "//div[4]/div/div[2]//div[@tabindex='0']"
    btn_select_job_category = "//*[contains(text(),'Professionals')]"
    btn_sub_unit = "//div[5]/div/div[2]//div[@tabindex='0']"
    btn_select_sub_unit = "//*[contains(text(),'Engineering')]"
    btn_location_path = "//div[6]/div/div[2]//div[@tabindex='0']"
    btn_select_location_path = "//*[contains(text(),'Texas R&D')]"
    btn_employementstatus_xpath = "//form[@class='oxd-form']/div/div/div[7]//i"
    btn_employeestatus_click_xpath = "//*[contains(text(),'Freelance')]"
    btn_jobsave_xpath = "//div[3]/button[@type='submit']"

    # salary
    link_salary_linktext = "Salary"
    btn_ad_salary = "//div[2]//div[1]//div[2]/div[1]//button[@type='button']"
    txt_salary_component = "//div[1]/div/div[2]/input"
    btn_pay_grade = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_select_pay_grade = "//*[contains(text(),'Grade 5')]"
    btn_pay_frequency = "//div[3]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_select_pay_frequency = "//*[contains(text(),'Hourly')]"
    btn_currency_path = "//div[4]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_select_currency = "//*[contains(text(),'United States Dollar')]"
    txt_amount_xpath = "//div[5]/div/div[2]/input"
    btn_save_salary = "//button[normalize-space()='Save']"

    # tax
    link_tax_linktext = "Tax Exemptions"
    btn_fed_status_xpath = "//form/div[1]//div[2]//div[@tabindex='0']"
    btn_fede_status_select_xpath = "//*[contains(text(),'Married')]"
    txt_fed_exemption_xpath = "//div[2]/div/div[2]//input"
    btn_state_status_xpath = "//div[2]/div/div[1]/div/div[2]/div/div/div[@tabindex='0']"
    btn_state_status_select_xpath = "//*[contains(text(),'Virginia')]"
    btn_status_drp_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    btn_status_drp_select_xpath = "//div[2]/div/div[2]//*[contains(text(),'Married')]"
    txt_state_txt_input = "//div[3]//div[2]/input"
    btn_unemp_xpath = "//form//div[4]//div[2]//div[@tabindex='0']"
    btn_unemp_select_xpath = "//*[contains(text(),'California')]"
    btn_work_state_xpath = "//form//div[5]//div[2]//div[@tabindex='0']"
    btn_work_select_xpath = "//*[contains(text(),'California')]"
    btn_savetax_xpath = "//button[normalize-space()='Save']"

    # report
    link_reportto_linktext = "Report-to"
    btn_add_report = "//div/div[2]/div[1]/div/button"
    txt_add_supervisr_name = "//input[@placeholder='Type for hints...']"
    btn_select1_name = "//*[contains(text(),'Linda Jane Anderson')]"
    btn_reporting_method = "//form/div[1]//div[2]//div[@tabindex='0']"
    btn_select_reporting_method = "//*[contains(text(),'Direct')]"
    btn_savesupervisor = "//button[normalize-space()='Save']"
    btn_addsuborinate_path = "//div/div[3]/div[1]/div/button"
    txt_subordinate_name = "//input[@placeholder='Type for hints...']"
    btn_select2_name = "//*[contains(text(),'Charlie  Carter')]"
    btn_reporting1_method = "//*[contains(text(),'-- Select --')]"
    btn_select_report_method = "//*[contains(text(),'Indirect')]"
    btn_savesubordinate = "//button[normalize-space()='Save']"

    # Qualification(work experience)
    link_qualification_linktext = "Qualifications"
    btn_add_work_exp = "//div[2]/div[2]/div[1]/div/button"
    txt_company_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_jobtitle_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_from_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_to_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_saveworkexp_xpath = "//button[@class ='oxd-button oxd-button--medium " \
                            "oxd-button--secondary orangehrm-left-space']"

    # qualification(Education)
    btn_educationadd_xpath = "//div[@class='orangehrm-edit-employee-content']//div[3]/" \
                             "div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button"
    btn_level_path = "//form/div[1]//div[2]//div[@tabindex='0']"
    btn_select_level_xpath = "//*[contains(text(),'College Undergraduate')]"
    txt_institute_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_major_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//input"
    txt_year_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//input"
    txt_gpa_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"
    txt_start_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_end_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_saveeducation_xpath = "//button[@class ='oxd-button oxd-button--medium " \
                            "oxd-button--secondary orangehrm-left-space']"

    # qualification(skills)
    btn_add_skills = "//div[4]/div[1]/div/button"
    btn_skill_path = "//form/div[1]//div[2]//div[@tabindex='0']"
    btn_select_skill_path = "//*[contains(text(),'Python')]"
    txt_year_of_experience = "//div[2]/div[2]//input"
    txt_skill_comments = "//textarea"
    btn_saveskills = "//button[normalize-space()='Save']"

    # qualification(language)
    btn_add_language_button = "//div[5]/div[1]/div/button"
    btn_language_xpath = "//form/div[1]/div/div[1]//div[@tabindex='0']"
    btn_select_language = "//*[contains(text(),'English')]"
    btn_fluency = "//form/div[1]/div/div[2]//div[@tabindex='0']"
    btn_select_fluency = "//*[contains(text(),'Speaking')]"
    btn_competency = "//form/div[1]/div/div[3]//div[@tabindex='0']"
    btn_select_competency = "//*[contains(text(),'Good')]"
    txt_language_comments = "//textarea"
    btn_savelanguage = "//button[normalize-space()='Save']"

    # qualification(license)
    btn_add_license = "//div[6]/div[1]/div/button"
    btn_license_type = "//form/div[1]/div/div[1]//div[@tabindex='0']"
    btn_select_license_type = "//*[contains(text(),'Certified Digital Marketing Professional')]"
    txt_license_no_xpath = "//div[2]//div[2]/input"
    txt_license_issued_date = "//form/div[2]/div/div[1]//input"
    txt_license_expiry_date = "//form/div[2]/div/div[2]//input"
    btn_savelicense = "//button[normalize-space()='Save']"

    # membership
    link_membership_linktext = "Memberships"
    btn_mem_add_xpath = "//div[1]/div/div[2]/div[1]/div/button"
    btn_memship_xpath = "//form/div/div/div[1]//div[@tabindex='0']"
    btn_mem_list_xpath = "//*[contains(text(),'CIMA')]"
    btn_subscription_xpath = "//form/div/div/div[2]//div[@tabindex='0']"
    btn_mem_subscription_xpath = "//*[contains(text(),'Individual')]"
    txt_subscription_amt_xpath = "//div[3]//div[2]//input"
    btn_currency_xpath = "//form/div/div/div[4]//div[@tabindex='0']"
    btn_mem_currency_xpath = "//*[contains(text(),'Indian Rupee')]"
    txt_sub_commence_date_xpath = "//div[5]//input[@placeholder='yyyy-mm-dd']"
    txt_sub_renewal_date_xpath = "//div[6]//input[@placeholder='yyyy-mm-dd']"
    btn_membership_save_xpath = "//button[@class ='oxd-button oxd-button--medium " \
                            "oxd-button--secondary orangehrm-left-space']"

    def __init__(self,driver):
        self.driver = driver

    def personal_details(self, nickname, otherid, licenseno, expirydate, ssn, sin, dob, militaryservice):
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).send_keys(nickname)
        self.driver.find_element(By.XPATH, self.txt_other_id_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.txt_license_no_path).send_keys(licenseno)
        self.driver.find_element(By.XPATH, self.txt_expiry_date_xpath).send_keys(expirydate)
        self.driver.find_element(By.XPATH, self.txt_ssn_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH, self.txt_sin_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH, self.txt_date_of_birth).send_keys(dob)
        self.driver.find_element(By.XPATH, self.btn_gender_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_nationality_click).click()
        self.driver.find_element(By.XPATH, self.txt_military_service_xpath).send_keys(militaryservice)
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_blood_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_blood_group).click()
        self.driver.find_element(By.XPATH, self.btn_save1_xpath).click()
        time.sleep(5)

    def contact_details(self, street1, street2, city, state, pincode, homephno, mobileno, work, email, otheremail):
        self.driver.find_element(By.LINK_TEXT, self.link_contact_linktxt).click()
        self.driver.find_element(By.XPATH, self.txt_street1_xpath).send_keys(street1)
        self.driver.find_element(By.XPATH, self.txt_street2_xpath).send_keys(street2)
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.txt_state_xpath).send_keys(state)
        self.driver.find_element(By.XPATH, self.txt_pincode_xpath).send_keys(pincode)
        self.driver.find_element(By.XPATH, self.btn_country_path_select).click()
        self.driver.find_element(By.XPATH, self.btn_country_click_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_homenumber_xpath).send_keys(homephno)
        self.driver.find_element(By.XPATH, self.txt_mobile_xpath).send_keys(mobileno)
        self.driver.find_element(By.XPATH, self.txt_work_xpath).send_keys(work)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.txt_workemail_xpath).send_keys(email)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.txt_othermail_xpath).send_keys(otheremail)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.txt_contactsave_xpath).click()
        time.sleep(3)

    def emergency_details(self, name, relationship, mobileno, workno):
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, self.link_emergency_linktxt).click()
        self.driver.find_element(By.XPATH, self.btn_add_contact).click()
        self.driver.find_element(By.XPATH, self.txt_name_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.txt_relationship_xpath).send_keys(relationship)
        self.driver.find_element(By.XPATH, self.txt_mobileno_xpath).send_keys(mobileno)
        self.driver.find_element(By.XPATH, self.txt_workno_xpath).send_keys(workno)
        self.driver.find_element(By.XPATH, self.btn_emergencycontactsave_xpath).click()

    def dependent(self, name1, dob1):
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, self.link_dependent_linktxt).click()
        self.driver.find_element(By.XPATH, self.btn_add_dependent).click()
        self.driver.find_element(By.XPATH, self.txt_dependentname_xpath).send_keys(name1)
        self.driver.find_element(By.XPATH, self.btn_relation_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_relation_click_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_add_dob_xpath).send_keys(dob1)
        self.driver.find_element(By.XPATH, self.btn_dependentsave_xpath).click()

    def immigration(self, number, issueddate1, expirydate1, eligiblestatus, reviewdate, command):
        self.driver.find_element(By.LINK_TEXT, self.link_immigration_linktxt).click()
        self.driver.find_element(By.XPATH, self.btn_add_immigration).click()
        self.driver.find_element(By.XPATH, self.txt_number_xpath).send_keys(number)
        self.driver.find_element(By.XPATH, self.txt_issueddate_xpath).send_keys(issueddate1)
        self.driver.find_element(By.XPATH, self.txt_expirydate_xpath).send_keys(expirydate1)
        self.driver.find_element(By.XPATH, self.txt_eligible_status_xpath).send_keys(eligiblestatus)
        self.driver.find_element(By.XPATH, self.btn_issuedby_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_issuedby_click_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_eligiblereview_xpath).send_keys(reviewdate)
        self.driver.find_element(By.XPATH, self.command_xpath).send_keys(command)
        self.driver.find_element(By.XPATH, self.btn_saveimmigration_xpath).click()

    def job_details(self, joineddate):
        self.driver.find_element(By.LINK_TEXT, self.link_job_linktext).click()
        self.driver.find_element(By.XPATH, self.txt_joineddate_xpath).send_keys(joineddate)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_drp_job_title_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_select_job_title).click()
        self.driver.find_element(By.XPATH, self.btn_drp_job_category).click()
        self.driver.find_element(By.XPATH, self.btn_select_job_category).click()
        self.driver.find_element(By.XPATH, self.btn_sub_unit).click()
        self.driver.find_element(By.XPATH, self.btn_select_sub_unit).click()
        self.driver.find_element(By.XPATH, self.btn_location_path).click()
        self.driver.find_element(By.XPATH, self.btn_select_location_path).click()
        self.driver.find_element(By.XPATH, self.btn_employementstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_employeestatus_click_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_jobsave_xpath).click()

    def salary_details(self, salcomponent, amount1, comments, acountno, routingno, amount2):
        self.driver.find_element(By.LINK_TEXT,self.link_salary_linktext).click()
        self.driver.find_element(By.XPATH, self.btn_ad_salary).click()
        self.driver.find_element(By.XPATH, self.txt_salary_component).send_keys(salcomponent)
        self.driver.find_element(By.XPATH, self.btn_pay_grade).click()
        self.driver.find_element(By.XPATH, self.btn_select_pay_grade).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_pay_frequency).click()
        self.driver.find_element(By.XPATH, self.btn_select_pay_frequency).click()
        self.driver.find_element(By.XPATH, self.btn_currency_path).click()
        self.driver.find_element(By.XPATH, self.btn_select_currency).click()
        self.driver.find_element(By.XPATH, self.txt_amount_xpath).send_keys(amount1)
        self.driver.find_element(By.XPATH, self.btn_save_salary).click()

    def tax_details(self, fedexamption, stateexemption):
        self.driver.find_element(By.LINK_TEXT, self.link_tax_linktext).click()
        self.driver.find_element(By.XPATH, self.btn_fed_status_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_fede_status_select_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_fed_exemption_xpath).send_keys(fedexamption)
        self.driver.find_element(By.XPATH, self.btn_state_status_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_state_status_select_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_status_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_state_status_select_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_state_txt_input).send_keys(stateexemption)
        self.driver.find_element(By.XPATH, self.btn_unemp_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_unemp_select_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_work_state_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_work_select_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_savetax_xpath).click()

    def report_to(self, suprname, subname):
        self.driver.find_element(By.LINK_TEXT, self.link_reportto_linktext).click()
        self.driver.find_element(By.XPATH, self.btn_add_report).click()

        self.driver.find_element(By.XPATH, self.txt_add_supervisr_name).send_keys(suprname)

        self.driver.find_element(By.XPATH, self.btn_select1_name).click()
        self.driver.find_element(By.XPATH, self.btn_reporting_method).click()
        self.driver.find_element(By.XPATH, self.btn_select_reporting_method).click()
        self.driver.find_element(By.XPATH, self.btn_savesupervisor).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_addsuborinate_path).click()
        self.driver.find_element(By.XPATH, self.txt_subordinate_name).send_keys(subname)
        self.driver.find_element(By.XPATH, self.btn_select2_name).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_reporting1_method).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_select_report_method).click()
        self.driver.find_element(By.XPATH, self.btn_savesubordinate).click()

    def qualification_wrk_experience(self, company, jobtitle, fromdate, todate, comments):
        self.driver.find_element(By.LINK_TEXT, self.link_qualification_linktext).click()
        self.driver.find_element(By.XPATH, self.btn_add_work_exp).click()
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(company)
        self.driver.find_element(By.XPATH, self.txt_jobtitle_xpath).send_keys(jobtitle)
        self.driver.find_element(By.XPATH, self.txt_from_xpath).send_keys(fromdate)
        self.driver.find_element(By.XPATH, self.txt_to_xpath).send_keys(todate)
        self.driver.find_element(By.XPATH, self.btn_saveworkexp_xpath).click()

    def qualification_education(self, institute, major, year, gpa, startdate, enddate):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_educationadd_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_level_path).click()
        self.driver.find_element(By.XPATH, self.btn_select_level_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_institute_xpath).send_keys(institute)
        self.driver.find_element(By.XPATH, self.txt_major_xpath).send_keys(major)
        self.driver.find_element(By.XPATH, self.txt_year_xpath).send_keys(year)
        self.driver.find_element(By.XPATH, self.txt_gpa_xpath).send_keys(gpa)
        self.driver.find_element(By.XPATH, self.txt_start_xpath).send_keys(startdate)
        self.driver.find_element(By.XPATH, self.txt_end_xpath).send_keys(enddate)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_saveeducation_xpath).click()

    def qualification_skills(self, yearofexp, comments):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_add_skills).click()
        self.driver.find_element(By.XPATH, self.btn_skill_path).click()
        self.driver.find_element(By.XPATH, self.btn_select_skill_path).click()
        self.driver.find_element(By.XPATH, self.txt_year_of_experience).send_keys(yearofexp)
        self.driver.find_element(By.XPATH, self.txt_skill_comments).send_keys(comments)
        self.driver.find_element(By.XPATH, self.btn_saveskills).click()

    def qualification_language(self, comments):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_add_language_button).click()
        self.driver.find_element(By.XPATH, self.btn_language_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_select_language).click()
        self.driver.find_element(By.XPATH, self.btn_fluency).click()
        self.driver.find_element(By.XPATH, self.btn_select_fluency).click()
        self.driver.find_element(By.XPATH, self.btn_competency).click()
        self.driver.find_element(By.XPATH, self.btn_select_competency).click()
        self.driver.find_element(By.XPATH, self.txt_language_comments).send_keys(comments)
        self.driver.find_element(By.XPATH, self.btn_savelanguage).click()

    def qualification_license(self, licenseno, issueddate, expirydate2):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_add_license).click()
        self.driver.find_element(By.XPATH, self.btn_license_type).click()
        self.driver.find_element(By.XPATH, self.btn_select_license_type).click()
        self.driver.find_element(By.XPATH, self.txt_license_no_xpath).send_keys(licenseno)
        self.driver.find_element(By.XPATH, self.txt_license_issued_date).send_keys(issueddate)
        self.driver.find_element(By.XPATH, self.txt_license_expiry_date).send_keys(expirydate2)
        self.driver.find_element(By.XPATH, self.btn_savelicense).click()

    def membership(self, supsamount, supscommencedate, renewaldate):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, self.link_membership_linktext).click()
        self.driver.find_element(By.XPATH, self.btn_mem_add_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_memship_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_mem_list_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_subscription_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_mem_subscription_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_subscription_amt_xpath).send_keys(supsamount)
        self.driver.find_element(By.XPATH, self.btn_currency_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_mem_currency_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_sub_commence_date_xpath).send_keys(supscommencedate)
        self.driver.find_element(By.XPATH, self.txt_sub_renewal_date_xpath).send_keys(renewaldate)
        self.driver.find_element(By.XPATH, self.btn_membership_save_xpath).click()
        time.sleep(5)
