# encoding=utf-8

import requests
import json

class AlertTo():
    def __init__(self):
        self.email = []
        self.rocket = []
        self.telegram = []

class Script():
    def __init__(self, name, command):
        self.name = name                      
        self.dir = ""                      
        self.command = command                      
        self.get = ""                      
        self.replicate = 1                      
        self.always = False                      
        self.disableAlert = False                      
        self.env = {}                      
        self.continuityInterval = 3600                   
        self.port = 0                              
        self.killTime = 1   
        self.loop = 0                           
        self.version = ""   
        self.disable = False                          
        # alert                 AlertTo           
        self.alert = AlertTo()


    def dump(self):
        # data = self.__dict__
        # print(self.alert.__dict__)
        self.alert = self.alert.__dict__
        return json.dumps( self.__dict__  )
        
