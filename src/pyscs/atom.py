from pydantic import BaseModel


class AtomSignal(BaseModel):
    timeout: int = 0          # 超时时间， 单位:s
    restart: bool = False            # 如果超时了是否重启
    notice: bool = False             # 如果超时了是否报警通知
    continuityInterval:int = 0   # 下次报警时间
    parameter:str = ""   # 回调参数
