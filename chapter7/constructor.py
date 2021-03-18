# constructor is also known as init method. and it's used in this formula "__int__" double underscore front and back. 

class Car():
    doors = 4
    wheels = 4

    def __init__(self):
        print('This is a constructor')

    def detail(self, name, color):
        return F'The car name is {name} and the color is {color} with {self.wheels} wheels and {self.doors} doors'

c1 = Car()