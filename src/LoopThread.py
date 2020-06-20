from PyQt5.QtCore import *
from GameClient import *

class LoopThread(QThread, GameClient):
    
    signal = pyqtSignal(str)
    
    def __init__(self):
        super(LoopThread, self).__init__()
        GameClient.__init__(self)
            
  
    def connect_(self, ip_address):
        while True:
            while True:
                try:
                    self.connect_to_server(ip_address)
                    break
                except Exception as arr:
                    print(arr)
                    break
            break       
        
    def run(self):
        while True:
            line = self.receive_message()
            if len(line): self.signal.emit(str(line)) 
            else: break