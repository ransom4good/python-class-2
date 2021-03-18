# A method is a function inside a Class. Every Methiod must have a "Self" in the class.

class Car():
    doors = 4
    wheels = 4

    def detail(self, name, color):
        return F'The car name is {name} and the color is {color} with {self.wheels} wheels and {self.doors} doors'

c1 = Car()
print(c1.doors)        
print(c1.wheels)        
print(c1.detail('BMW', 'BLACK'))  

c2 = Car()
print(c2.detail('Toyota', 'Red'))