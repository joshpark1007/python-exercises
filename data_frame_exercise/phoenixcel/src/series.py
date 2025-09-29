class Series(list):
    def sum(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self)

    avg = average

    def apply(self, func):
        self = Series([func(x) for x in self])
        return self
