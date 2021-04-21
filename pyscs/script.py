# encoding=utf-8

import requests
import json
import copy
from pyscs.alertto import AlertTo



class Cron():
    def __init__(self):
        self.start = ""
        self.loop = 0
        self.isMonth = False


class LookPath():
    def __init__(self):
        self.command = ""
        self.path = ""
        self.install = ""

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
        self.update = "git pull"
        self.deleteWhenExit = False                      
        self.version = ""
        self.disable = False                          
        # alert                 AlertTo           
        self.alert = AlertTo()
        self.cron = Cron()
        self.lookPath = []

    def add_lookPath(self, params: LookPath):
        self.lookPath.append(params.dump())

    def dump(self):
        # data = self.__dict__
        # print(self.alert.__dict__)
        script = copy.deepcopy(self.__dict__) 
        script["alert"] = self.alert.dump()
        script["cron"] = self.cron.__dict__
        for lp in self.lookPath:
            if lp:
                script["lookPath"].append(lp.__dict__)
        # alter = self.alert.dump()
        # self.cron = self.__class__.cron.__dict__
        return script
        
