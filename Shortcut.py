# coding:UTF-8
from gloVar import gloVar


class Shortcut:
    def __init__(self):
        self.name = "Shortcut"
        
    def login(self, url, userId, password):
        gloVar.common.get(url)
        gloVar.common.maximizeWindow()
        gloVar.common.PageObject.LoginPage.userId().sendKeys(userId)
        gloVar.common.PageObject.LoginPage.password().sendPassword(password)
        gloVar.common.PageObject.LoginPage.loginButton().click()

    def loginProxy(self, userId):
        gloVar.common.PageObject.Menu.Tab("主页")
        gloVar.common.PageObject.HomePage.LeftNavigation().SearchArea().SearchField().sendKeys(userId)
        gloVar.common.PageObject.HomePage.LeftNavigation().SearchArea().SearchButton().click()

        gloVar.common.PageObject.HomePage.SearchResultArea().link(userId).click()

        gloVar.common.PageObject.PreLoginPage.TopArea().LoginButton().click()