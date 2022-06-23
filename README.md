# Python3 lib for scs

> python version > = 3.10


```python
from pyscs.scs import SCS

scs = SCS()
# set script can be stop right now
msg, code = scs.can_stop()
if code == 200:
    print("success")
elif code == 201:
    print("warning: " + msg)
else:
    print(msg)

# set script can not be stop except exec scs.can_stop()
msg, code = scs.can_not_stop()
if code == 200:
    print("success")
elif code == 201:
    print("warning: " + msg)
else:
    print(msg)


from pyscs import Script
# add script or server
s = Script("test", "python test.py")
# When dir is not empty and is not exist and get is not empty, It will command get first
s.dir = "/home/test"
s.get = "cd /home && git clone xxxx"
msg, code = scs.add_script(s)
if code == 200:
    print("success")
elif code == 201:
    print("warning: " + msg)
else:
    print(msg)

# del script or server on scsd
# test is pname
msg, code = scs.del_script("test")
if code == 200:
    print("success")
elif code == 201:
    print("warning: " + msg)
else:
    print(msg)



# set alert like add script

a = Alert()
# When dir is not empty and is not exist and get is not empty, It will command get first
a.pname = "alert"
a.name = "test"
a.title = "some thing broken"
a.broken = True
a.reason = "error"
msg, code = scs.set_alert(a)
if code == 200:
    print("success")
elif code == 201:
    print("warning: " + msg)
else:
    print(msg)
```