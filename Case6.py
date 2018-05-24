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

        common.PageObject.Menu.MoreTabs_Tab().click()
        common.PageObject.Menu.MoreTabs_Tab().Item("日常工作计划").click()

        common.PageObject.DailyWorkPlanPage.newButton().click()

        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.saveButton().click()
        
        actualStartTimeList = common.PageObject.CreatePlanPage.startTime().options().getText()
        expectStartTimeList = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        actualEndTimeList = common.PageObject.CreatePlanPage.endTime().options().getText()
        expectEndTimeList = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        actualWorkContentList = common.PageObject.CreatePlanPage.workContent().options().getText()
        expectWorkContentList = ["--无--", "制定月度活动计划", "活动方案/流程策划", "与第三方机构洽谈合作", "讲者邀约沟通", "场地勘测/沟通", "营业沟通（买赠/人员/物料）", "活动前消费者邀约", "活动文件/物料准备", "场地布置/活动彩排", "执行消费者活动（P-class/PS）", "活动后跟进-文件整理/ 报销结算", "协助营业的CS活动"]

        return1 = common.Assert.List.equals(expectStartTimeList, actualStartTimeList)
        return2 = common.Assert.List.equals(expectEndTimeList, actualEndTimeList)
        return3 = common.Assert.List.equals(expectWorkContentList, actualWorkContentList)
        return4 = common.Assert.String.equals(common.PageObject.CreatePlanPage.errorMsg("开始日期").getText(), "错误: 必须输入一个值")
        return5 = common.Assert.String.equals(common.PageObject.CreatePlanPage.errorMsg("工作内容").getText(), "错误: 必须输入一个值")

        logStep("StartTimeList Check", return1)
        logStep("EndTimeList Check", return2)
        logStep("WorkContentList Check", return3)
        logStep("StartDate Empty Check", return4)
        logStep("WorkContent Empty Check", return5)

        date = datetime.now() + timedelta(days=0)
        year = str(int(date.strftime('%Y')))
        month = str(int(date.strftime('%m')))
        day = str(int(date.strftime('%d')))
        startDate = year + '-' + month + '-' + day
        startTime = "09:00"
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
        common.capture("")

        return6 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText(), planType)
        return7 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始日期").getText(), startDate)
        return8 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("开始时间").getText(), startTime)
        return9 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("工作内容").getText(), workContent)
        return10 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText(), status)
        return11 = common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("结束时间").getText(), endTime)

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