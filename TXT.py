# coding:UTF-8
from gloVar import gloVar

class TXT:
    def __init__(self, path):
        self.path = path

    def read(self):
        f = open(self.path)
        result = f.read()
        f.close
        return result

    def write(self, msg):
        f = open(self.path, "w")
        f.write(msg)
        f.close

    def add(self, msg):
        f = open(self.path)
        orgMsg = f.read().decode("utf-8")
        f.close
        f = codecs.open(self.path, "w", 'utf-8')
        f.write(orgMsg)
        f.write("\n")
        f.write(msg)
        f.close