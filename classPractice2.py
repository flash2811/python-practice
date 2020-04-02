class Employee:
    #class variable
    raiseAmount = 1.04
    numOfEmps = 0;

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@gmail.com'

        Employee.numOfEmps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

emp_1 = Employee('John','Smith',50000)
emp_2 = Employee('Subhra', 'Mondal', 60000)


print(emp_1.email)
print(emp_2.email)

print(emp_2.fullName())

print(emp_2.pay)
emp_2.applyRaise()
print(emp_2.pay)

Employee.raiseAmount = 1.05
emp_2.applyRaise()
print(emp_2.pay)

