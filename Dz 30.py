class Counter:
    current = 0

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        # print(self.current) # --> 0
        # print(self.start) # --> 0
        # print(self.end) # --> 20

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            return 'Out of range'

my_count=Counter(start=0, end=9)
print(my_count.increase())
print(my_count.increase())
print(my_count.increase())
print(my_count.increase())