# encoding = utf - 8
import unittest
import os
from Common import Common
from gloVar import gloVar
import time
from datetime import datetime, timedelta


__author__ = "Yuanzhuang Gao"
__version__ = "1.0"
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

        testdata = common.dataJSON.read()[gloVar.caseName]

        url = testdata["url"]
        userId = testdata["userId"]
        password = testdata["password"]
        common.Shortcut.login(url, userId, password)

        common.PageObject.Menu.MoreTabs_Tab().click()
        common.PageObject.Menu.MoreTabs_Tab().Item("日常工作计划").click()

        common.PageObject.DailyWorkPlanPage.newButton().click()
        common.PageObject.CreatePlanPage.table().click()

        date = datetime.now() + timedelta(days=1)
        year = str(int(date.strftime('%Y')))
        month = str(int(date.strftime('%m')))
        day = str(int(date.strftime('%d')))
        startDate = year + '-' + month + '-' + day
        startTime = "09:00"
        endTime = "19:00"
        workContent = "制定月度活动计划"
        status = "未填写实际123"
        planType = "计划内"

        common.PageObject.CreatePlanPage.startDate().sendKeys(startDate)
        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.startTime().select(startTime)
        common.PageObject.CreatePlanPage.endTime().select(endTime)
        common.PageObject.CreatePlanPage.workContent().select(workContent)
        common.PageObject.CreatePlanPage.saveButton().click()
        # common.capture("")

        return6 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText(), planType)
        return7 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始日期").getText(), startDate)
        return8 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始时间").getText(), startTime)
        return9 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("工作内容").getText(), workContent)
        return10 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText(), status)
        return11 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("结束时间").getText(), endTime)

        logStep("planType Check", return6)
        logStep("startDate Check", return7)
        logStep("startTime Check", return8)
        logStep("workContent Empty Check", return9)
        logStep("status Empty Check", return10)
        logStep("endTime Empty Check", return11)

    def logStep(self, desc, result):
        gloVar.log.logStep(desc, result)
        self.assertEqual(result, True, desc + " -- Fail --")
		
if __name__ == "__main__":
    unittest.main()