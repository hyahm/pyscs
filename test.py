# encoding = utf-8

from pyscs.scs import SCS
from pyscs.script import Script
from pyscs.alert import Alert


class BBBB():
    server = ""
    url = ""

# s = Script("test", "python test.py")
# s.dir = ""
# scs = SCS(domain="https://192.168.50.50:11111")
# # scs.add_script(s)
# alert = Alert()
# alert.name = "test"
# alert.pname = "test"
# alert.reason = "test alret"
# alert.title = "test alert"
# ok = scs.set_alert(alert)
# print(ok)


class AAAA():
    pname = ""
    def __init__(self):
        self.name = ""
        self.to = BBBB()
    
    def print(self):
        print(self.__class__.pname)
    to = BBBB()
    
aaa = AAAA()
aaa.to.url = "https://www.baidu.com"
aaa.to = aaa.to.__dict__
print(type(aaa))
if isinstance(aaa, AAAA):
    print("is class")
print(aaa.__dict__)
aaa.print()