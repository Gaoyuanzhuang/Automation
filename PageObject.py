# coding:UTF-8
import mjn


class PageObject:
    def __init__(self):
        self.name = "PageObject"
        self.LoginPage = mjn.LoginPage()
        self.Menu = mjn.Menu()
        self.DailyWorkPlanPage = mjn.DailyWorkPlanPage()
        self.CreatePlanPage = mjn.CreatePlanPage()
        self.ModifyPlanPage = mjn.ModifyPlanPage()
        self.DailyWorkPlanDetailInformation = mjn.DailyWorkPlanDetailInformation()
        self.InputRecordPage=mjn.InputRecordPage()
        self.HomePage = mjn.HomePage()
        self.PreLoginPage = mjn.PreLoginPage()
        self.TopBar = mjn.TopBar()
