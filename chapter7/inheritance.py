class Employee():
    pay_raise = 0.10
    # 10 percent can also be written as 10/100

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p
        return increment + self.p

# make use of the syntax "Pass" to leave a class without a property. 
class Developer(Employee):
    def staff_details(self):
        return F'firstname {self.f}, lastname {self.l}'

d1 = Developer('Emmanuel', 'Adebayo', 2000)
print(d1.staff_details())
print(d1.f)
print(d1.l)
print(d1.salary())


d2 = Developer('Mercy', 'Adekola', 4000)
print(d2.staff_details())
print(d2.f)
print(d2.l)
print(d2.salary())