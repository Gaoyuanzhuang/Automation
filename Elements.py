# coding:UTF-8
from gloVar import gloVar


class Elements:
    def __init__(self, locator, name):
        # gloVar.driver.switch_to.frame("top")
        self.eles = gloVar.driver.find_elements_by_xpath(locator)
        self.name = name
        self.locator = locator

    def getText(self):
        result = []
        isFirst = True
        txtForLog = "["
        for ele in self.eles:
            txt = ele.text
            if isFirst:
                isFirst = False
                txtForLog = txtForLog + "\"" + txt + "\""
            else:
                txtForLog = txtForLog + ", \"" + txt + "\""
            result.append(txt)
        txtForLog = txtForLog + "]"
        gloVar.log.add(self.name + ".getText() : " + txtForLog)
        return result
