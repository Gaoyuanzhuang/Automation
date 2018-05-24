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

        # Login
        testdata = common.dataJSON.read()[gloVar.caseName]

        url = testdata["url"]
        userId = testdata["userId"]
        password = testdata["password"]
        
        common.Shortcut.login(url, userId, password)

        # 新建数据
        common.PageObject.Menu.MoreTabs_Tab().click()
        common.PageObject.Menu.MoreTabs_Tab().Item("日常工作计划").click()
        common.PageObject.DailyWorkPlanPage.newButton().click()

        # 参数赋值
        date = datetime.now() + timedelta(days=1)
        year = str(int(date.strftime('%Y')))
        month = str(int(date.strftime('%m')))
        day = str(int(date.strftime('%d')))
        startDate = year + '-' + month + '-' + day
        startTime = "15:00"
        endTime = "19:00"
        workContent = "制定月度活动计划"
        status = "未填写实际"
        planType = "计划内"
        common.PageObject.CreatePlanPage.startDate().sendKeys(startDate)
        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.startTime().select(startTime)
        common.PageObject.CreatePlanPage.endTime().select(endTime)
        common.PageObject.CreatePlanPage.workContent().select(workContent)
        common.capture("新建计划填入的内容")
        common.PageObject.CreatePlanPage.saveButton().click()
        common.capture("新建计划保存后内容展示")

        # 新建数据结果断言
        return1 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText(), planType)
        return2 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始日期").getText(), startDate)
        return3 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始时间").getText(), startTime)
        return4 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("工作内容").getText(), workContent)
        return5 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText(), status)
        return6 = common.Assert.String.equals(
            common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("结束时间").getText(), endTime)
        logStep("planType Check", return1)
        logStep("startDate Check", return2)
        logStep("startTime Check", return3)
        logStep("workContent Empty Check", return4)
        logStep("status Empty Check", return5)
        logStep("endTime Empty Check", return6)

        # 数据修改
        common.PageObject.DailyWorkPlanDetailInformation.modifyButton().click()
        common.switchAlertAccept()

        # 校验修改页面信息是否与原计划填入信息一致
        return7 = common.Assert.String.equals(common.PageObject.ModifyPlanPage.startDate().getAttribute("value"), startDate)
        return8 = common.Assert.String.equals(common.PageObject.ModifyPlanPage.startTime().selectedOption().getText(),startTime)
        return9 = common.Assert.String.equals(common.PageObject.ModifyPlanPage.endTime().selectedOption().getText(),endTime)
        return10 = common.Assert.String.equals(common.PageObject.ModifyPlanPage.workContent().selectedOption().getText(), workContent)
        logStep("startDate Check", return7)
        logStep("startTime Check", return8)
        logStep("endTime Check", return9)
        logStep("workContent Empty Check", return10)

        # 验证取消按钮功能
        common.PageObject.ModifyPlanPage.cancelButton().click()
        return11 = common.PageObject.DailyWorkPlanDetailInformation.modifyButton().isDisplayed()
        gloVar.log.logStep("Cancel button", return11)

        # 验证数据修改保存
        common.PageObject.DailyWorkPlanDetailInformation.modifyButton().click()
        common.switchAlertAccept()

        startTime = "10:00"
        endTime = "20:00"
        workContent = "活动文件/物料准备"

        common.PageObject.ModifyPlanPage.startTime().select(startTime)
        common.PageObject.ModifyPlanPage.endTime().select(endTime)
        common.PageObject.ModifyPlanPage.table().click()
        common.PageObject.ModifyPlanPage.workContent().select(workContent)
        common.capture("数据修改项内容展示")
        common.PageObject.ModifyPlanPage.saveButton().click()
        common.capture("数据修改保存后内容展示")

        return11 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText(), planType)
        return12 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始日期").getText(), startDate)
        return13 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始时间").getText(), startTime)
        return14 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("工作内容").getText(), workContent)
        return15 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText(), status)
        return16 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("结束时间").getText(), endTime)

        logStep("planType Check", return11)
        logStep("startDate Check", return12)
        logStep("startTime Check", return13)
        logStep("workContent Empty Check", return14)
        logStep("status Empty Check", return15)
        logStep("endTime Empty Check", return16)

        # 校验修改历史纪录是否正确
        common.PageObject.DailyWorkPlanDetailInformation.historyTable().tr(1).td("操作").getText()

    def logStep(self, desc, result):
        gloVar.log.logStep(desc, result)
        self.assertEqual(result, True, desc + " -- Fail --")

if __name__ == "__main__":
    unittest.main()