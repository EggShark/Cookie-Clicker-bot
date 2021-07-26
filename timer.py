
import time

class CodeTimer:
    
    def __init__(self):
        self.clearTimer()

    # Put this at the begining of the function or whatever code you want to test
    def codeBegining(self):
        self.begining = time.time()

    # Put this at the end of whatever code you want to time
    def codeEnd(self):
        self.end = time.time()

    # This will return how much time it took to run the code in between codeBegining() and codeEnd()
    def getCodeTime(self):
        return self.end - self.begining
    
    def clearTimer(self):
        pass
    #ty Zach -EggMan