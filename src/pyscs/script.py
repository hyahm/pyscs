# encoding=utf-8

import copy
from pyscs.alertto import AlertTo



class Cron():
    def __init__(self):
        self.start = ""
        self.loop = 0
        self.isMonth = False
        self.times = 0


class PreStart():
    def __init__(self):
        self.command = ""
        self.path = ""
        self.install = ""
        self.gt = ""
        self.ge = ""
        self.le = ""
        self.le = ""
        self.eq = ""
        self.ne = ""
        self.separation = ""
        self.execCommand = ""
        self.template = ""

    def dump(self):
        return self.__dict__

class Script():
    def __init__(self, name, command):
        self.name = name                      
        self.dir = ""                      
        self.command = command                      
        self.replicate = 0                   
        self.always = False                      
        self.disableAlert = False                      
        self.env = {}                      
        self.continuityInterval = 0                   
        self.port = 0                              
        self.update = ""
        self.deleteWhenExit = False                      
        self.version = ""
        self.disable = False                          
        # alert                 AlertTo           
        self.alert = AlertTo()
        self.cron = Cron()
        self.preStart = []

    def add_preStart(self, preStart: PreStart):
        self.preStart.append(preStart.dump())

    def dump(self):
        # data = self.__dict__
        # print(self.alert.__dict__)
        script = copy.deepcopy(self.__dict__) 
        script["alert"] = self.alert.dump()
        script["cron"] = self.cron.__dict__
        for lp in self.preStart:
            if lp:
                script["preStart"].append(lp.__dict__)
        return script
        
