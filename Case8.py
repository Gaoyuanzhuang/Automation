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

        common.PageObject.ModifyPlanPage.cancelButton()

        date = datetime.now() 
        year = str(int(date.strftime('%Y')))
        month = str(int(date.strftime('%m')))
        day = str(int(date.strftime('%d')))
        startDate = year + '-' + month + '-' + day
        startTime="12:00"
        endTime="15:00"
        workContent="讲者邀约沟通"
        common.PageObject.CreatePlanPage.startDate().sendKeys(startDate)
        common.PageObject.CreatePlanPage.table().click()
        common.PageObject.CreatePlanPage.startTime().select(startTime)
        common.PageObject.CreatePlanPage.endTime().select(endTime)
        common.PageObject.CreatePlanPage.workContent().select(workContent)
        common.PageObject.CreatePlanPage.saveButton().click()

        return1=common.PageObject.DailyWorkPlanDetailInformation.planNo().isDisplayed()
        return2=common.Assert.String.equals(common.PageObject.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText(), "计划外")
        logStep('Create plan',return1)
        logStep('PlanType check',return2)
        #获取planNo
        planNo=common.PageObject.DailyWorkPlanDetailInformation.planNo().getText()

        #Step2点击【日常工作计划】，选择已创建成功的计划外 – 日常工作计划
        #planNo='A-000470'
        common.PageObject.Menu.MoreTabs_Tab().click()
        common.PageObject.Menu.MoreTabs_Tab().Item("日常工作计划").click()
        common.PageObject.DailyWorkPlanPage.Projectlink(planNo).click()
        logStep('Step2-进入计划详细信息展示页面',True)
        common.capture('进入详情')


        #Step3点击填写记录
        common.PageObject.DailyWorkPlanDetailInformation.inputRecord().click()
        common.switchAlertAccept()
        logStep('Step3-进入填写页面',True)
        common.capture('填写页面')

        #Step4 验证计划信息模块
        return3=common.PageObject.InputRecordPage.planDate().isDisplayed()
        return4=common.PageObject.InputRecordPage.planStartTime().isDisplayed()
        return5=common.PageObject.InputRecordPage.planEndTime().isDisplayed() 
        return6=common.PageObject.InputRecordPage.planContent().isDisplayed()
        logStep('Step4-验证开始日期是否显示',return3)
        logStep('Step4-验证开始时间是否显示',return4)
        logStep('Step4-验证工作内容是否显示',return5)
        logStep('Step4-验证结束时间是否显示',return6)

        #验证实际信息模块
        return7=common.PageObject.InputRecordPage.actualDate().isDisplayed()
        return8=common.PageObject.InputRecordPage.actualStartTime().isDisplayed()
        return9=common.PageObject.InputRecordPage.actualEndTime().isDisplayed()
        return10=common.PageObject.InputRecordPage.actualContent().isDisplayed() 
        return11=common.PageObject.InputRecordPage.actionReason().isDisplayed()
        return12=common.PageObject.InputRecordPage.actualStatus().isDisplayed()
        logStep('Step4-验证开始日期是否显示',return7)
        logStep('Step4-验证开始时间是否显示',return8)
        logStep('Step4-验证结束时间是否显示',return9)
        logStep('Step4-验证工作内容是否显示',return10)
        logStep('Step4-验证完成情况是否显示',return11)
        logStep('Step4-验证原因备注是否显示',return12)

        #Step5-验证字段不可修改
        return13=common.PageObject.InputRecordPage.planDate().getAttribute("readonly")
        logStep('Step5-验证开始日期是否可修改',return13)

        #Step6-“开始时间”下拉列表，验证下拉列表值01:00 ~ 24:00(间隔半小时)
        actualStartTimeList = common.PageObject.InputRecordPage.planStartTime().options()
        expectStartTimeList = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        return14 = common.Assert.List.equals(expectStartTimeList, actualStartTimeList)
        logStep('Step6-验证下拉菜单',return14)

        #Step7-“结束时间”下拉列表，验证下拉列表值01:00 ~ 24:00(间隔半小时)
        actualEndTimeList = common.PageObject.InputRecordPage.planEndTime().options()
        expectEndTimeList = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        return15 = common.Assert.List.equals(expectEndTimeList, actualEndTimeList)
        logStep('Step7-验证下拉菜单',return15)

        #Step8-验证工作内容下拉菜单
        actualWorkContentList = common.PageObject.InputRecordPage.planContent().options()
        expectWorkContentList = ["", "制定月度活动计划", "活动方案/流程策划", "与第三方机构洽谈合作", "讲者邀约沟通", "场地勘测/沟通", "营业沟通（买赠/人员/物料）", "活动前消费者邀约", "活动文件/物料准备", "场地布置/活动彩排", "执行消费者活动（P-class/PS）", "活动后跟进-文件整理/ 报销结算", "协助营业的CS活动"]
        return16 = common.Assert.List.equals(expectWorkContentList, actualWorkContentList)
        logStep('Step8-验证下拉菜单',return16)

        #Step9-验证字段不可修改
        return13=common.PageObject.InputRecordPage.actualDate().getAttribute("readonly")
        logStep('Step9-验证开始日期是否可修改',return13)

        #Step10-“开始时间”下拉列表，验证下拉列表值01:00 ~ 24:00(间隔半小时)
        actualStartTimeList1 = common.PageObject.InputRecordPage.actualStartTime().options()
        gloVar.log.add(actualStartTimeList1)
        expectStartTimeList1 = ["", "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        return17 = common.Assert.List.equals(actualStartTimeList1, expectStartTimeList1)
        logStep('Step10-验证下拉菜单',return17)

        #Step11-“结束时间”下拉列表，验证下拉列表值01:00 ~ 24:00(间隔半小时)
        actualEndTimeList1 = common.PageObject.InputRecordPage.actualEndTime().options()
        gloVar.log.add(actualEndTimeList1)
        expectEndTimeList1= ["", "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
        return18 = common.Assert.List.equals(expectEndTimeList1, actualEndTimeList1)
        logStep('Step11-验证下拉菜单',return18)

        #Step12-验证工作内容下拉菜单
        actualWorkContentList1 = common.PageObject.InputRecordPage.actualContent().options()
        gloVar.log.add(actualWorkContentList1)
        expectWorkContentList1 = ["", "制定月度活动计划", "活动方案/流程策划", "与第三方机构洽谈合作", "讲者邀约沟通", "场地勘测/沟通", "营业沟通（买赠/人员/物料）", "活动前消费者邀约", "活动文件/物料准备", "场地布置/活动彩排", "执行消费者活动（P-class/PS）", "活动后跟进-文件整理/ 报销结算", "协助营业的CS活动"]
        return19 = common.Assert.List.equals(expectWorkContentList1, actualWorkContentList1)
        logStep('Step12-验证下拉菜单',return19)

        #Step13-验证完成情况下拉菜单
        actualWorkStatus1 = common.PageObject.InputRecordPage.actualStatus().options()
        gloVar.log.add(actualWorkStatus1)
        expectWorkStatus1 = ["无执行", "进展顺利", "进展迟缓", "已完成"]
        return20 = common.Assert.List.equals(expectWorkStatus1, actualWorkStatus1)
        logStep('Step13-验证下拉菜单',return20)

        #Step14-填写记录，信息填写不完整，无法保存
        common.PageObject.InputRecordPage.actualStatus().select('无执行')
        common.PageObject.InputRecordPage.saveButton().click()
        return21=common.PageObject.InputRecordPage.errormsg().isDisplayed()
        common.capture('错误提示')
        logStep('Step14-验证必填校验',return21)
        common.PageObject.InputRecordPage.actualStartTime().select('12:00')
        common.PageObject.InputRecordPage.actualEndTime().select('13:00')
        common.PageObject.InputRecordPage.actualContent().select('制定月度活动计划')
        common.PageObject.InputRecordPage.saveButton().click()
        return22=common.PageObject.InputRecordPage.errormsg2().getText()=='当完成情况为“无执行”时，原因备注必须填写'
        common.capture('错误提示2')
        logStep('Step15-验证必填校验',return22)

        #Step15-填写记录，保存成功
        common.PageObject.InputRecordPage.actualStartTime().select('12:00')
        common.PageObject.InputRecordPage.actualEndTime().select('13:00')
        common.PageObject.InputRecordPage.actualContent().select('制定月度活动计划')
        common.PageObject.InputRecordPage.actualStatus().select('进展顺利')
        common.PageObject.InputRecordPage.saveButton().click()
        return22=common.PageObject.DailyWorkPlanDetailInformation.table('计划信息').field('状态').getText()=='已填写实际'
        common.capture('填写完成')
        logStep('Step15-验证是否保存成功',return22)

        #Step16-再次点击填写记录
        common.PageObject.DailyWorkPlanDetailInformation.inputRecord().click()
        common.switchAlertAccept()
        logStep('Step16-进入填写页面',True)

        #Step17-输入原因备注，保存成功
        common.PageObject.InputRecordPage.actualStartTime().select('12:00')
        common.PageObject.InputRecordPage.actualEndTime().select('13:00')
        common.PageObject.InputRecordPage.actualContent().select('制定月度活动计划')
        common.PageObject.InputRecordPage.actualStatus().select('无执行')
        common.PageObject.InputRecordPage.actionReason().sendKeys('测试测试')
        common.PageObject.InputRecordPage.saveButton().click()
        return23=common.PageObject.DailyWorkPlanDetailInformation.table('实际信息').field('完成情况').getText()=='无执行' and common.PageObject.DailyWorkPlanDetailInformation.table('实际信息').field('原因备注').getText()=='测试测试'
        

    def logStep(self, desc, result):
        gloVar.log.logStep(desc, result)
        self.assertEqual(result, True, desc + " -- Fail --")

if __name__ == "__main__":
    unittest.main()