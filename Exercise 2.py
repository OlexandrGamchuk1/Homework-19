class Numbers:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return f'Numbers: {self.n1}, {self.n2}'

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('not an integer entered')
        self.__dict__[key] = value

n = Numbers(3, 3)
print(n)