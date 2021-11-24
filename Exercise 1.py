class My_Descriptor:
    def __init__(self, text):
        self.text = text

    def __get__(self, instance_self, instance_class):
        return self.text

    def __set__(self, instance_self, value):
        raise AttributeError("field is read-only")

    def __delete__(self, instance):
        raise AttributeError("cannot delete field")

class Text:
    text = My_Descriptor('Hello')

    def __str__(self):
        return str(self.text)

a = Text()
print(a.text)
del a.text