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

class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super(). __init__ (first_name, last_name, pay)
        self.prog = prog_lang
        self.email = F'{self.l}.{self.f}@alabiansolutions.com'
        self.form_email = self.email.lower()
        
    def staff_details(self):
        return F'firstname {self.f}, lastname {self.l}'

d1 = Developer('Goodluck', 'Jonathan', 2000, 'Python')
print(d1.prog)
print(d1.form_email)

d2 = Developer('Ransom', 'Adekola', 5000, 'Jango',)
print(d2.prog)
print(d2.form_email.upper())