# encoding = utf-8

from pyscs import SCS, Script, Alert
import time

scs = SCS(domain="http://127.0.0.1:11111")
s = Script("test", "python3 test.py")
s.always = True
s.dir = "/data/scs"
s.replicate = 3

resp = scs.add_script(s)

print(resp)
# # scs.add_script(s)
# alert = Alert()
# alert.name = "test"
# alert.pname = "test"
# alert.reason = "test alret"
# alert.title = "test alert"
# ok = scs.set_alert(alert)
# print(ok)

# t = TTT()
# for i in range(10000000):
#     time.sleep(1)
#     t.send("%d error" % i)