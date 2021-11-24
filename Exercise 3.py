import time
class Names:
    def __init__(self, __name):
        self.__name = __name

    def get_name(self):
        return self.__name

    def set_name(self, name_value):
        with open('text.txt', 'w') as file:
            file.write(f'{name_value} -> {time.ctime()}\n')
        self.__name = name_value

    name = property(get_name, set_name)

name1 = Names('')
name1.name = 'Ivan'
print(name1.name)