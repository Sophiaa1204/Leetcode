class Logger:

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.dict.keys():
            if timestamp - self.dict[message] >= 10:
                self.dict[message] = timestamp
                return True
            else:
                return False
        else:
            self.dict[message] = timestamp
            return True