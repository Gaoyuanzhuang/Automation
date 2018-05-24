# encoding = utf - 8
import unittest
import os
from Common import Common
from gloVar import gloVar
import time
from datetime import datetime, timedelta


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化类固件"""
        print("----setUpClass")

    @classmethod
    def tearDownClass(cls):
        """重构类固件"""
        print("----tearDownClass")

    # 初始化工作
    def setUp(self):
        print("--setUp")
        # Get the current file name which will be output to the log
        gloVar.caseName = os.path.basename(__file__)[:-3]
        # Initial automation script
        self.common = Common()
        gloVar.common = self.common
        self.common.timeOut(30)

    # 退出清除工作
    def tearDown(self):
        print("--tearDown")
        gloVar.log.logCase()
        self.common.closeWindow()

    def testScenario(self):
        common = self.common
        logStep = self.logStep

        # Login
        testdata = common.dataJSON.read()[gloVar.caseName]

        url = testdata["url"]
        userId = testdata["userId"]
        password = testdata["password"]
        
        common.Shortcut.login(url, userId, password)

        #数据准备：创建计划，计划类型为计划外
        common.PageObject.Menu.MoreTabs_Tab().click()
        common.PageObject.Menu.MoreTabs_Tab().Item("日常工作计划").click()
        common.PageObject.DailyWorkPlanPage.newButton().click()
        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.saveButton().click()


        date = datetime.now() 
        year = str(int(date.strftime('%Y')))
        month = str(int(date.strftime('%m')))
        day = str(int(date.strftime('%d')))
        startDate = year + '-' + month + '-' + day
        startTime = "17:30"
        endTime = "19:00"
        workContent = "制定月度活动计划"
        status = "未填写实际"
        planType = "计划外"

        common.PageObject.CreatePlanPage.startDate().sendKeys(startDate)
        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.startTime().select(startTime)
        common.PageObject.CreatePlanPage.endTime().select(endTime)
        common.PageObject.CreatePlanPage.workContent().select(workContent)
        common.PageObject.CreatePlanPage.saveButton().click()
        common.capture("计划内数据创建成功")


        common.PageObject.DailyWorkPlanDetailInformation.cancel().click()
        common.switchAlertAccept()
        return10 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText(), "已取消")
        gloVar.log.logStep("status Check", return10)
        return11 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.historyTable().tr(1).td("操作").getText(), "将 状态 从 未填写实际 更改至 已取消")
        gloVar.log.logStep("status Check", return11)
        common.capture("断言_计划信息_状态,日常工作计划历史_操作")    

    def logStep(self, desc, result):
        gloVar.log.logStep(desc, result)
        self.assertEqual(result, True, desc + " -- Fail --")

if __name__ == "__main__":
    unittest.main()