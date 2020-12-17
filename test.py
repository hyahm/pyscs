from pyscs.scs import SCS
from pyscs.script import Script
from pyscs.alert import Alert

s = Script("test", "python test.py")
s.dir = ""
scs = SCS()
scs.add_script(s)