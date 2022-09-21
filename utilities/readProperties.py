from jproperties import Properties

config = Properties()

with open("C:\\UmaRaniDundigalla\\UmaRani_workspace\\GUVI\\GUVI_Project1\\Configurations\\config.properties", 'rb') as configFile:
    config.load(configFile)



class ReadConfig:

    @staticmethod
    def getAppUrl():
        url = config.get("baseURL").data
        return url

    @staticmethod
    def getUsername():
        username = config.get("username").data
        return username

    @staticmethod
    def getPassword():
        password = config.get("password").data
        return password

    @staticmethod
    def getFirstName():
        firstname = config.get("firstname").data
        return firstname

    @staticmethod
    def getMiddleName():
        middlename = config.get("middlename")
        return middlename

    @staticmethod
    def getLastName():
        lastname = config.get("lastname").data
        return lastname


    @staticmethod
    def getEmployeeName():
        employeename = config.get("employeename").data
        return employeename

    @staticmethod
    def getUserName1():
        username1 = config.get("username1").data
        return username1

    @staticmethod
    def getPassword1():
        password1 = config.get("password1").data
        return password1








