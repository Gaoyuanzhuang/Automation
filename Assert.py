# coding:UTF-8
from gloVar import gloVar
import unittest
# import sys
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

class Assert:
    def __init__(self):
        self.name = "Assert"
        self.List = List()
        self.String = String()

    def equals(arg1, arg2):
        if arg1 == arg1:
            gloVar.log.add(self.name + ".equals(" + ExpectArg + ")" + " : " + "TRUE")
        else:
            gloVar.log.add(self.name + ".equals(" + ExpectArg + ")" + " : " + "FALSE")


class List:
    def __init__(self):
        self.name = "List"

    def equals(self, arg1, arg2):
        result = True
        if len(arg1) == len(arg2):
            for i in range(0, len(arg1)-1):
                if arg1[i] != arg2[i]:
                    result = False
                    break
        else:
            result = False
        return result


class String:
    def __init__(self):
        self.name = "String"

    def equals(self, arg1, arg2):
        result = True
        if arg1 == arg2:
            result = True
        else:
            result = False
        return result
