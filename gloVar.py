class gloVar:
    #global driver
    global currentWindowHandle
    global log
    global caseName
    global pathPyFramework
    global pathPyFrameworkCapture
    global pathPyFrameworkCommon
    global pathPyFrameworkPageObject
    global pathPyFrameworkTC
    global pathPyFrameworkLog
    global testResult
    global TCResultFile

    def __init__(self):
        self.name = "List"
        self.logTCResult = "C:\Python3\Scripts\MJN\TCResult.txt"

    def getLogTCResult(self):
        return self.logTCResult
