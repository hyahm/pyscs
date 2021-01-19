# encoding=utf-8
from pyscs.script import AlertTo
import copy

class Alert():
    def __init__(self):
        self.title = ""
        self.pname = ""
        self.name = ""
        self.reason = ""
        self.broken = False
        self.interval = 10
        self.to = AlertTo()
        
        
    def dump(self):
        alert = copy.deepcopy(self.__dict__) 
        alert["to"] = self.to.__dict__
        return alert
    
