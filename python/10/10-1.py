class MathTest:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second if self.second != 0 else None
    
test = MathTest(2, 4)
print(test.add())
print(test.sub())
print(test.mul())
print(test.div())
