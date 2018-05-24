# coding:UTF-8
from selenium import webdriver
from gloVar import gloVar
from selenium.common.exceptions import NoSuchElementException
import Elements

class Element:
    def __init__(self, locator, name):
        # gloVar.driver.switch_to.frame("top")
        self.name = name
        self.locator = locator

    def sendKeys(self, txt):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        self.ele.click()
        self.ele.clear()
        self.ele.send_keys(txt)
        str = ".send_keys(" + txt + ")"
        # str = str.decode("utf-8", 'ignore')
        gloVar.log.add(self.name + str)
		
    def sendPassword(self, txt):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        self.ele.click()
        self.ele.clear()
        self.ele.send_keys(txt)
        str = ".sendPassword(******)"
        # str = str.decode("utf-8", 'ignore')
        gloVar.log.add(self.name + str)

    def click(self):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        # self.name = self.name.decode("utf-8", 'ignore')
        self.ele.click()
        gloVar.log.add(self.name + ".click()")

    def select(self, keyword):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        self.ele.click()
        self.optionEle = gloVar.driver.find_element_by_xpath(self.locator + "/option[contains(text(),'" + keyword + "')]")
        self.optionEle.click()
        str = ".select(" + keyword + ")"
        # str = str.decode("utf-8", 'ignore')
        gloVar.log.add(self.name + str)

    def options(self):
        select = gloVar.driver.find_element_by_xpath(self.locator)
        options_list = select.find_elements_by_tag_name("option")
        options_value=[]
        for option in options_list:
            options_value.append(option.get_attribute("value"))  
        return options_value

    def getAttribute(self, keyword):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        result=self.ele.get_attribute(keyword)
        str = ".getAttribute(" + keyword + ")"
        # str = str.decode("utf-8", 'ignore')
        gloVar.log.add(self.name + str + " : " + result)
        return result

    def getText(self):
        try:
            gloVar.driver.implicitly_wait(2)
            self.ele = gloVar.driver.find_element_by_xpath(self.locator)
            # self.name = self.name.decode("utf-8", 'ignore')
            result = self.ele.text
            gloVar.log.add(self.name + ".getText() : " + result)
            gloVar.driver.implicitly_wait(30)
            return result
        except NoSuchElementException as msg:
            # gloVar.log.add(self.name + ".getText() : Exception " + msg)
            # self.name = self.name.decode("utf-8", 'ignore')
            gloVar.log.add(self.name + ".getText() : " + "")
            gloVar.driver.implicitly_wait(30)
            return ""
        else:
            self.name = self.name.decode("utf-8", 'ignore')
            # gloVar.log.add(self.name + ".getText() : " + "")
            gloVar.driver.implicitly_wait(30)
            return ""

    def isDisplayed(self):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        result = self.ele.is_displayed()
        gloVar.log.add(self.name + ".isDisplayed() : " + str(result))
        return result

    def getTagName(self):
        self.ele = gloVar.driver.find_element_by_xpath(self.locator)
        result = self.ele.tag_name
        gloVar.log.add(self.name + ".getTagName() : " + result)
        return result

    
