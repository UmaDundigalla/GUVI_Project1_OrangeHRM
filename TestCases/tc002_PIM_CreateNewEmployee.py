import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.PIM import CreateNewEmployee
from PageObjects.PIM_NewEmployee_personaldetails import NewEmployee_Personal_Detail


def random_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_CreateEmployee:

    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

#pim
    firstname = ReadConfig.getFirstName()
    middlename = ReadConfig.getMiddleName()
    lastname = ReadConfig.getLastName()
    photo = "TestData//user_image.png"

#pim personal details
    nickname = "dundigalla"
    otherid = "888"
    licenseno1 = "789"
    expirydate = "2024-04-30"
    ssn = "456-789-456"
    sin = "909012456"
    dob = "1988-04-30"
    militaryservice = "no"

#pim contact details
    street1 = "street no-4,Banjara hills"
    street2 = "Road no 12"
    city = "Hyderabad"
    state = "Telangana"
    pincode = "500008"
    homephno = "9756642587"
    mobileno = "9752145633"
    work = "8579212396"
    email = random_generator(1) + "@gmail.com"
    otheremail = random_generator(2) + "@gmail.com"

#pim emergency details
    name = "prem"
    relationship = "Father"
    mobilenum = "8754695213"
    workno = "7546932157"

#pim dependent
    name1 = "priya"
    relation = "daughter"
    dob1 = "2018-11-02"

#pim immigration
    number = "7456982312"
    issueddate1 = "2015-07-01"
    expirydate1 = "2023-07-01"
    eligiblestatus = "Eligible"
    reviewdate = "2022-01-01"
    comments1 = "success"

#pim job
    joineddate = "2018-04-2"

#pim salary details
    salcomponent = "hike"
    amount1 = "35000"
    comments2 = "this is my salary"
    acountno = "87452369995"
    routingno = "874"
    amount2 = "12000"

    # tax
    fedexamption = "62"
    stateexemption = "25"

    # report to
    suprname = "L"
    subname = "C"

    # qualification(workexperience)
    company = "zzzcorporation"
    jobtitle = "seniorofficer"
    fromdate = "2017-07-15"
    todate = "2022-04-19"
    comments3 = "work experience"

    # qualification(eduction)
    institute = "cmeccollege"
    major = "ANE"
    year = "2010"
    gpa = "3.6"
    startdate = "2018-05-30"
    enddate = "2022-05-26"
    # qualification(skills)
    yearofexp = "3"
    comments4 = "skills"
    # qualification(language)
    comments5 = "languages"
    # qualification(license)
    licenseno2 = "777"
    issueddate = "2016-10-24"
    expirydate2 = "2024-04-30"

    # membership
    supsamount = "15000"
    supscommencedate = "2022-01-12"
    renewaldate = "2024-04-30"

    logger = LogGen.loggen()


    def test_create_employee(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        lp = Login_Page(self.driver)
        self.driver.implicitly_wait(10)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        emp = CreateNewEmployee(self.driver)
        self.logger.info("********tc002 PIM-Creating New Employee******")
        emp.pim(self.firstname, self.lastname, self.photo)
        self.logger.info("*******New Employee is Created*****")
        detail1 = NewEmployee_Personal_Detail(self.driver)
        time.sleep(10)
        detail1.personal_details(self.nickname,self.otherid,self.licenseno1,self.expirydate,self.ssn,self.sin,self.dob,self.militaryservice)
        self.logger.info("*******Personal Details are added*******")
        self.driver.execute_script("window.scrollBy(0,-2000)", "")
        detail2 = NewEmployee_Personal_Detail(self.driver)
        detail2.contact_details(self.street1,self.street2,self.city,self.state,self.pincode,self.homephno,self.mobileno,self.work,self.email,self.otheremail)
        self.logger.info("******Contact Details are added********")
        detail3 = NewEmployee_Personal_Detail(self.driver)
        detail3.emergency_details(self.name,self.relationship,self.mobilenum,self.workno)
        self.logger.info("******Emergency Details are added********")
        detail4 = NewEmployee_Personal_Detail(self.driver)
        detail4.dependent(self.name1, self.dob1)
        self.logger.info("********Dependent is Added******")
        detail5 = NewEmployee_Personal_Detail(self.driver)
        detail5.immigration(self.number,self.issueddate1,self.expirydate1,self.eligiblestatus,self.reviewdate,self.comments1)
        self.logger.info("********Immigration Details are Added******")
        detail6 = NewEmployee_Personal_Detail(self.driver)
        detail6.job_details(self.joineddate)
        self.logger.info("******Job Details are Added*******")
        detail7 = NewEmployee_Personal_Detail(self.driver)
        detail7.salary_details(self.salcomponent,self.amount1,self.comments2,self.acountno,self.routingno,self.amount2)
        self.logger.info("*******Salary Details are Added********")
        details8 = NewEmployee_Personal_Detail(self.driver)
        details8.tax_details(self.fedexamption,self.stateexemption)
        self.logger.info("*******Tax Details are Added********")
        details9 = NewEmployee_Personal_Detail(self.driver)
        details9.report_to(self.suprname, self.subname)
        self.logger.info("******Reports are included*******")
        details10 = NewEmployee_Personal_Detail(self.driver)
        details10.qualification_wrk_experience(self.company,self.jobtitle,self.fromdate,self.todate,self.comments3)
        self.logger.info("*******Work Experience is added******")
        details11 = NewEmployee_Personal_Detail(self.driver)
        details11.qualification_education(self.institute,self.major,self.year,self.gpa,self.startdate,self.enddate)
        self.logger.info("********Education is added*******")
        details12 = NewEmployee_Personal_Detail(self.driver)
        details12.qualification_skills(self.yearofexp,self.comments4)
        self.logger.info("********Skills are added*******")
        details13 = NewEmployee_Personal_Detail(self.driver)
        details13.qualification_language(self.comments5)
        self.logger.info("********Languages are added*******")
        details14 = NewEmployee_Personal_Detail(self.driver)
        details14.qualification_license(self.licenseno2,self.issueddate,self.expirydate2)
        self.logger.info("********License Details are added*******")
        self.driver.execute_script("window.scrollBy(0,-2000)", "")
        details15 = NewEmployee_Personal_Detail(self.driver)
        details15.membership(self.supsamount,self.supscommencedate,self.renewaldate)
        self.logger.info("*******Membership is added******")
        self.logger.info("******Ending tc002_PIM_CreateNewEmployee******")


