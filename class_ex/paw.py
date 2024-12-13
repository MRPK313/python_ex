


class PowTwo:

    def __init__(self, max_pow) -> None:
        self.n = 0
        self.max_pow = max_pow

    
    def __iter__(self):
        return self
    

    def __next__(self):

        if self.n <= self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration
        


p = PowTwo(5)
print(next(p))
print(next(p))
print(next(p))
for i in p:
    print(i)

