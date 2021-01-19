# encoding=utf-8

import requests
import os
from pyscs.script import Script
import json

class SCS:
    def __init__(self, domain="https://127.0.0.1:11111", pname=None, name=None, token=None):
        requests.packages.urllib3.disable_warnings()
        if pname is None:
            pname = os.getenv("PNAME", "")
        if name is None:
            name = os.getenv("NAME", "")
        
        if token is None:
            token = os.getenv("TOKEN", "")
        self._domain = domain
        self._pname = pname
        self._name = name
        self._token = token
        self._headers = {
            "Token": self._token
        }
    
    def get_pname(self):
        return self._pname
    
    def get_name(self):
        return self._name
    
    def get_token(self):
        return self._token
    
    def _post(self, url, data=None):
        if isinstance(data, dict):
            data = json.dumps(data)
        try:
            r = requests.post(self._domain + url, verify=False, data=data, headers=self._headers,timeout=5)
        except Exception as e:
            return e, 0
        if r.status_code != 200:
            return r.status_code, 0
        try:
            d = r.json()
        except Exception as e:
            return r.text, 0
        return  d["msg"], d["code"]
        
    def can_stop(self, name=""):
        if name == "":
            name = self._name
        if name == "":
            return "name is empty", 0
        return self._post("/canstop/" + name)
    
    def can_not_stop(self, name=""):
        if name == "":
            name = self._name
        if name == "":
            return "name is empty", 0
        # data = '{"pname":"%s", "name": "%s", "value": true}' % (self._pname, self._name)
        return self._post("/cannotstop/" + name)
    
    def add_script(self, script: Script):
        """
        add script
        scs = SCS("https://127.0.0.1:11111", "mm", "mm_0", "sadfasdg1654346098")
        s = Script("aa", "ls")
        msg, ok = scs.add_script(s)
        if not ok:
            print(msg) 
            
        print("ok: " + msg)
        
        # name               string          
        # dir                string          
        # command            string           
        # replicate          int              
        # always             bool             
        # disableAlert       bool              
        # env                map[string]string 
        # continuityInterval int     
        # port               int               
        # alert                 AlertTo           
        # version            string   
        """
        if script.name == "" or script.command == "":
            return "name and command is empty", 0
        return self._post("/script", script.dump())
        
    
    def del_script(self, pname):
        return self._post("/delete/" + pname)
    
    def set_alert(self, alert):
        if alert.pname == "":
            alert.pname = self._pname
        if alert.name == "":
            alert.name = self._name
        return self._post("/set/alert", alert.dump())