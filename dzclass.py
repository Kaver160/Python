class Human:
    def __init__(self, age = 19, name = 'Danik'):
        self.age=age
        self.name=name
    def say_hellow(self):
        return'hellow my names is {name}'.format(name = self.name)
class Builder(Human):
    def __init__(self,dolz='programist'):
        self.dolz=dolz
        super().__init__()
    def say_hellow(self):
        return'hellow my names is {name}, {dolz}'.format(name=self.name, dolz= self.dolz)
class Writer(Human):
    def my_books(*args):
        slovar = [element for element in args if type(element) ==str]
        return 'I write {} books'. format(len(slovar))
        pass
Sten = Writer(name = 'Sten li der')
print(Sten.my_books('Iron man, spider man, ffafas '))
