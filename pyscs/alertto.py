# encoding = utf-8

class AlertTo():
    def __init__(self):
        self.email = []
        self.rocket = []
        self.telegram = []
        self.weixin = []
        self.callback=[]

    def dump(self):
        # at = {}
        # at["email"] = self.email.dump()
        # at["rocket"] = self.rocket.dump()
        # at["telegram"] = self.telegram.dump()
        # at["weixin"] = self.weixin.dump()
        # self.rocket = self.rocket.dump()
        # self.telegram = self.telegram.dump()
        # self.weixin = self.weixin.dump()
        return self.__dict__