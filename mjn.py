# coding:UTF-8
from selenium import webdriver
from gloVar import gloVar
from Element import Element
from Elements import Elements

class LoginPage:
    def __init__(self):
        self.name = "LoginPage"

    def userId(self):
        return Element("//input[@id='username']",self.name + "." + "userId")

    def password(self):
        return Element("//input[@id='password']",self.name + "." + "password")

    def loginButton(self):
        return Element("//input[@id='Login']",self.name + "." + "Login")


class TopBar:
    def __init__(self):
        self.name = "TopBar"

    def userNav(self):
        return userNav("//div[@id='userNav']",self.name + "." + "userNav")


# TopBar > userNav
class userNav(Element):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def LogoffIcon(self):
        return LeftNavigationSearchArea("//a[text()='退出']", self.name + "." + "LogoffIcon")


class HomePage:
    def __init__(self):
        self.name = "HomePage"

    def LeftNavigation(self):
        return LeftNavigation("//td[@id='sidebarCell']", self.name + "." + "LeftNavigation")

    def SearchResultArea(self):
        return SearchResultArea("//h1[text()='搜索结果']/ancestor::td[@id='bodyCell']", self.name + "." + "SearchResultArea")   

# HomePage > LeftNavigation
class LeftNavigation(Element):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def SearchArea(self):
        return LeftNavigationSearchArea("//label[text()='搜索']/ancestor::form[1]", self.name + "." + "SearchArea")


# HomePage > LeftNavigation > SearchArea
class LeftNavigationSearchArea(Element):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def SearchField(self):
        return Element(self.locator + "//input[@id='sbstr']", self.name + "." + "SearchField")

    def SearchButton(self):
        return Element(self.locator + "//input[@name='search']", self.name + "." + "SearchButton")

# HomePage > SearchResultArea
class SearchResultArea(Element):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def link(self, keyword):
        return Element(self.locator + "//a[text()='" + keyword + "']", self.name + "." + "link(" + keyword + ")")


class PreLoginPage:
    def __init__(self):
        self.name = "PreLoginPage"

    def TopArea(self):
        return TopArea("//td[@id='topButtonRow']", self.name + "." + "TopArea")


# PreLoginPage > TopArea
class TopArea:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def LoginButton(self):
        return Tab("//input[@name='login']", self.name + "." + "LoginButton")


class Menu:
    def __init__(self):
        self.name = "Menu"

    def Tab(self, keyword):
        return Element("//ul[@id='tabBar']//a[text()='主页']", self.name + "." + "Tab(" + keyword + ")")

    def MoreTabs_Tab(self):
        return Tab("//li[@id='MoreTabs_Tab']/a", self.name + "." + "MoreTabs_Tab")


# Menu > Tab
class Tab(Element):
    def __init__(self, locator, name):
        self.locator = locator + "/.."
        self.name = name
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def Item(self, keyword):
        # keyword = keyword.decode("utf-8", 'ignore')
        return Element(self.locator + "//a[text()='" + keyword + "']", self.name + "." + "Item(" + keyword + ")")


class DailyWorkPlanPage:
    def __init__(self):
        self.name = "DailyWorkPlanPage"

    def newButton(self):
        return Element("//input[contains(@value,'新建')]",self.name + "." + "newButton")

    def Projectlink(self,keyword):
        return Element("//table[@class='list']//a[contains(text(),'"+keyword+"')]",self.name + "." + "Projectlink")

class CreatePlanPage:
    def __init__(self):
        self.name = "CreatePlanPage"

    def saveButton(self):
        return Element("//input[@name='page:form:pageblock:j_id6:bottom:j_id7']", self.name + "." + "saveButton")

    def startDate(self):
        return Element("//input[@id='page:form:pageblock:PlanInfo:j_id9:Plan_Date__c']", self.name + "." + "startDate")

    def startTime(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id13:Plan_Start_Time__c']", self.name + "." + "startTime")

    def endTime(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id16:Plan_End_Time__c']", self.name + "." + "endTime")

    def workContent(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id19:Plan_Content__c']", self.name + "." + "workContent")

    def table(self):
        return Element("//table[contains(@class,'detailList')]",self.name + "." + "table")

    def errorMsg(self, keyword):
        return Element("//label[contains(text(),'" + keyword + "')]/ancestor::th[1]/following::td[1]//div[@class='errorMsg']",self.name + "." + "errorMsg(" + keyword + ")")

   

# CreatePlanPage > SelectWebElement
class SelectWebElement(Element):
    def __init__(self, locator, name):
        self.name = name
        self.locator = locator
        self.ele = gloVar.driver.find_element_by_xpath(locator)

    def options(self):
        return Elements(self.locator + "/option", self.name + "." + "options")

    def selectedOption(self):
        return Element(self.locator + "/option[@selected = 'selected']",self.name + "." + "selectedOption")


class DailyWorkPlanDetailInformation:
    def __init__(self):
        self.name = "DailyWorkPlanDetailInformation"

    def table(self, keyword):
        # keyword = keyword.decode("utf-8", 'ignore')
        return DailyWorkPlanDetailInformationTable("//h3[text()='" + keyword  + "']/ancestor::div[contains(@class,'brandTertiaryBrd')]/following::div[1]",self.name + "." + "table(" + keyword + ")")

    def modifyButton(self):
        return Element("//input[contains(@value,'修改计划')]",self.name + "." + "modifyButton")

    def planNo(self):
        return Element("//h2[@class='pageDescription']",self.name + "." + "planNo")

    def inputRecord(self):
        return Element("//td[@id='topButtonRow']//input[@title='填写记录']",self.name + "." + "inputRecord")
    
    def cancel(self):
        return Element("//*[@id='bottomButtonRow']/input[contains(@value,'取消计划')]",self.name + "." + "cancel")
        
    def historyTable(self):
        return table("//h3[text()='日常工作计划历史']/ancestor::table[1]/following::table[1]",self.name + "." + "historyTable")    

# DailyWorkPlanDetailInformation > DailyWorkPlanDetailInformationTable
class DailyWorkPlanDetailInformationTable(Element):
    def __init__(self, locator, name):
        self.name = "Table"
        self.ele = gloVar.driver.find_element_by_xpath(locator)
        self.name = name
        self.locator = locator

    def field(self, keyword):
        # keyword = keyword.decode("utf-8", 'ignore')
        return Element(self.locator + "//td[text()='" + keyword + "']/following::td[1]",self.name + "." + "field(" + keyword + ")")

class ModifyPlanPage:
    def __init__(self):
        self.name = "ModifyPlanPage"

    def saveButton(self):
        return Element("//input[contains(@value,'保存')]", self.name + "." + "saveButton")

    def cancelButton(self):
        return Element("//input[contains(@value,'取消')]", self.name + "." + "cancelButton")

    def startDate(self):
        return Element("//input[@id='page:form:pageblock:PlanInfo:j_id9:Plan_Date__c']", self.name + "." + "startDate")

    def startTime(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id13:Plan_Start_Time__c']", self.name + "." + "startTime")

    def endTime(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id16:Plan_End_Time__c']", self.name + "." + "endTime")

    def workContent(self):
        return SelectWebElement("//select[@id='page:form:pageblock:PlanInfo:j_id19:Plan_Content__c']", self.name + "." + "workContent")

    def table(self):
        return Element("//table[contains(@class,'detailList')]",self.name + "." + "table")

class InputRecordPage:
    def __init__(self):
        self.name = "InputRecordPage"

    def planDate(self):
        return Element("//input[@id='page:form:pageblock:PlanInfo:j_id9:Plan_Date__c']",self.name + "." + "planDate")

    def planStartTime(self):
        return Element("//select[@id='page:form:pageblock:PlanInfo:j_id13:Plan_Start_Time__c']",self.name + "." + "planStartTime")    

    def planEndTime(self):
        return Element("//select[@id='page:form:pageblock:PlanInfo:j_id16:Plan_End_Time__c']",self.name + "." + "planEndTime") 

    def planContent(self):
        return Element("//select[@id='page:form:pageblock:PlanInfo:j_id19:Plan_Content__c']",self.name + "." + "planContent")  

    def actualDate(self):
        return Element("//input[@id='page:form:pageblock:ActualInfo:j_id22:Actual_Date__c']",self.name + "." + "actualDate")

    def actualStartTime(self):
        return Element("//select[@id='page:form:pageblock:ActualInfo:j_id26:Actual_Start_Time__c']",self.name + "." + "actualStartTime")    

    def actualEndTime(self):
        return Element("//select[@id='page:form:pageblock:ActualInfo:j_id29:Actual_End_Time__c']",self.name + "." + "actualEndTime") 

    def actualContent(self):
        return Element("//select[@id='page:form:pageblock:ActualInfo:j_id32:Actual_Content__c']",self.name + "." + "actualContent")    

    def actionReason(self):
        return Element("//textarea[@id='page:form:pageblock:ActualInfo:j_id35:No_Action_Reason__c']",self.name + "." + "actionReason") 

    def actualStatus(self):
        return Element("//select[@id='page:form:pageblock:ActualInfo:j_id38:Status__c']",self.name + "." + "actualStatus")          

    def saveButton(self):
        return Element("//input[contains(@value,'保存')]", self.name + "." + "saveButton")      

    def errormsg(self):
        return Element("//select[@id='page:form:pageblock:ActualInfo:j_id26:Actual_Start_Time__c']/following::div[@class='errorMsg'][1]",self.name+"."+"errormsg")

    def errormsg2(self):
        return Element("//div[@id='errorMessagediv']",self.name+"."+"errormsg2")    

# table
class table(Element):
    def __init__(self, locator, name):
        self.name = name
        self.locator = locator
        self.ele = gloVar.driver.find_element_by_xpath(locator)
        self.ths = gloVar.driver.find_elements_by_xpath(locator + "//tr[@class='headerRow']/th")

    def tr(self, keyword):
        if type(keyword) == str:
            index = 0
            for th in self.ths:
                index = index + 1
                if th.text.find(keyword) >= 0:
                    break
            return tr(self.locator + "//tr[contains(@class, 'dataRow')][" + str[index] + "]", self.name + "." + "tr[" + keyword + "]", self.ths)
        if type(keyword) == int:
            return tr(self.locator + "//tr[contains(@class, 'dataRow')][" + str(keyword) + "]", self.name + "." + "tr[" + str(keyword) + "]", self.ths)

class tr(Element):
    def __init__(self, locator, name, ths):
        self.name = name
        self.locator = locator
        self.ele = gloVar.driver.find_element_by_xpath(locator)
        self.ths = ths

    def td(self, keyword):
        if type(keyword) == str:
            index = 0
            for th in self.ths:
                index = index + 1
                if th.text == keyword:
                    break
            return Element(self.locator + "//*[" + str(index) + "]", self.name + "." + "td[" + keyword + "]")
        if type(keyword) == int:
            return Element(self.locator + "//*[" + str(keyword) + "]", self.name + "." + "td[" + str(keyword) + "]")
