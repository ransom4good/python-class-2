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

e1 = Employee('Ransom', 'Kuti', 30000)

# changing a value in a class
e1.f = 'Mercy'
print(e1.f)
print(e1.salary())

e2 = Employee('Rebecca', 'Umorin', 6000)
print(e2.salary())