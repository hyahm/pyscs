# encoding=utf-8

import requests
import os
from pyscs.script import Script
import json
from typing import Tuple, Dict, TypeVar, Union



class SCS:
    def __init__(self, domain="https://127.0.0.1:11111", pname: str=None, 
        name: str=None, token: str=None, debug: bool=False):
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
        self._debug=debug
        self._token = token
        self._headers = {
            "Token": self._token
        }
    
    def get_pname(self) -> None:
        return self._pname
    
    def get_name(self)-> None:
        return self._name
    
    def get_token(self)-> None:
        return self._token
    
    def _post(self, url, data=None)-> Union[Dict|str, bool]:
        if isinstance(data, dict):
            data = json.dumps(data)
        try:
            if self._debug:
                print(self._domain + url)
                print(data)
            r = requests.post(self._domain + url, verify=False, data=data, headers=self._headers,timeout=5)
            if r.status_code != 200:
                return (r.status_code, False)
            d = r.json()
        except Exception as e:
            return (e.args[0], False)
        return  (d["msg"], d["code"] == 200)
        
    def can_stop(self, name="")-> Union[Dict|str, bool]:
        if name == "":
            name = self._name
        if name == "":
            return "name is empty", 0
        return self._post("/canstop/" + name)
    
    def can_not_stop(self, name="")-> Union[Dict|str, bool]:
        if name == "":
            name = self._name
        if name == "":
            return "name is empty", 0
        # data = '{"pname":"%s", "name": "%s", "value": true}' % (self._pname, self._name)
        return self._post("/cannotstop/" + name)
    

    def status(self)-> Union[Dict|str, bool]:
        return self._post("/status")        


    def add_script(self, script: Script) -> Union[Dict|str, bool]:
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
        # port               int               
        # alert                 AlertTo           
        # version            string   
        """
        if script.name == "" or script.command == "":
            return "name and command is empty", 0
        return self._post("/script", script.dump())
        
    
    def del_script(self, pname)-> Union[Dict|str, bool]:
        return self._post("/delete/" + pname)
    
    def set_alert(self, alert)-> Union[Dict|str, bool]:
        if alert.pname == "":
            alert.pname = self._pname
        if alert.name == "":
            alert.name = self._name
        return self._post("/set/alert", alert.dump())