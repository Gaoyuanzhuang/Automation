# _*_ coding: utf-8 _*_  
import logging    
import logging.handlers
import gloVar
from TXT import TXT
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
  
class Logger(object):  
  
    def __init__(self, logger, path):  
        ''''' 
            指定保存日志的文件路径，日志级别，以及调用文件 
            将日志存入到指定的文件中 
        '''  
        # 创建一个logger  
        self.logger = logging.getLogger(logger)  
        self.logger.setLevel(logging.INFO)  
        self.testName = logger
        self.TCResultFile = TXT("C:\Python3\Scripts\MJN\TCResult.txt")
  
        # 创建一个handler，用于写入日志文件  
        fh =logging.handlers.TimedRotatingFileHandler(path,when='midnight', interval=1, backupCount=2, encoding='utf-8')
        fh.suffix="%Y-%m-%d.log"
  
        # 再创建一个handler，用于输出到控制台  
        ch = logging.StreamHandler()  
  
        # 定义handler的输出格式  
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')  
        fh.setFormatter(formatter)  
        ch.setFormatter(formatter)  
  
        # 给logger添加handler  
        self.logger.addHandler(fh)  
        self.logger.addHandler(ch)   
        # file_hanlder = logging.FileHandler(path, encoding='utf-8')  
        # self.logger.addHandler(file_hanlder) 
    def start(self):
        self.logger.info("-----------------开始执行-----------------")   
        gloVar.testResult = "PASS"

    def add(self, msg):
        self.logger.info(msg)

    def errorinfo(self):
        self.logger.error('error', exc_info=1)    

    def logStep(self, description, result):
        if result:
            set_color(FOREGROUND_GREEN)
            self.logger.info(description + " : " + "Pass")
            self.TCResultFile.write(self.testName + ":" + "PASS")
            set_color(FOREGROUND_WHITE)
        else:
            set_color(FOREGROUND_RED)
            self.logger.info(description + " : " + "Fail")
            self.TCResultFile.write(self.testName + ":" + "FAIL")
            set_color(FOREGROUND_WHITE)

    def logCase(self):
        self.logger.info("-----------------End Execution-----------------")
        if self.TCResultFile.read() == self.testName + ":" + "PASS":
            set_color(FOREGROUND_GREEN|FOREGROUND_INTENSITY)
            self.logger.info(self.testName + " : " + "Pass")
            set_color(FOREGROUND_WHITE)
        else:
            set_color(FOREGROUND_RED|FOREGROUND_INTENSITY)
            self.logger.info(self.testName + " : " + "Fail")
            set_color(FOREGROUND_WHITE)
        self.logger.info("-----------------------------------------")
        # gloVar.testResult to TXT   
