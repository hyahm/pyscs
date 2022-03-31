# encoding = utf-8

from src.pyscs import SCS, Script


scs = SCS(domain="https://127.0.0.1:11111", token="4>G^C(QSvOJ9||vIw,*4WEgSi8V^w_B", debug=True)
# s = Script("test", "python3 test.py")
# # s.always = True
# s.always = False
# s.dir = "E:\\code\\scs"
# s.replicate = 3

# resp = scs.add_script(s)
# print(resp, flush=True)

res, ok = scs.status()
print(res)
print(ok)
