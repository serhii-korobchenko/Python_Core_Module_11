class Iterable:
    
    def __init__(self):
        self.current_value = 0
        self.max_value = 10

    def __iter__(self):
        
        return self
        
    
    def __next__(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            return self.current_value
        raise StopIteration


c = Iterable()
for i in c:
    print(i)
