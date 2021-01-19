# encoding = utf-8

from pyscs.scs import SCS
from pyscs.script import Script
from pyscs.alert import Alert
import time

s = Script("test", "python3 test.py")
s.dir = "/data/scs"
s.replicate = 3

# resp = scs.add_script(s)

class TTT():
    def __init__(self):
        self.scs = SCS(domain="https://192.168.0.90:11111")
        self.alert = Alert()
        self.alert.name = "test"
        self.alert.pname = "test"
        self.alert.title = "aaaa"
    
    def send(self, msg=""):
        self.alert.reason = msg
        self.alert.interval
        resp = self.scs.set_alert(self.alert)
# resp = scs.can_stop("test_0")
# resp = scs.del_script("test")
        print(resp)
# # scs.add_script(s)
# alert = Alert()
# alert.name = "test"
# alert.pname = "test"
# alert.reason = "test alret"
# alert.title = "test alert"
# ok = scs.set_alert(alert)
# print(ok)

t = TTT()
for i in range(10000000):
    time.sleep(1)
    t.send("%d error" % i)


