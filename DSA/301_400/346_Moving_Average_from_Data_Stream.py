class MovingAverage:

    def __init__(self, size: int):
        self.data = []
        self.size = size
        self.volume = 0

    def next(self, val: int) -> float:
        if self.volume < self.size:
            self.volume += 1
            self.data.append(val)
            return sum(self.data) / self.volume
        else:
            self.data.pop(0)
            self.data.append(val)
            return sum(self.data) / self.volume