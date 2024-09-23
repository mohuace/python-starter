class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def tax(self):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30

    #This is an example of method overloading
    #In python, method overloading is implicit rather than explicit
    def demo(self, a=None, b=None, c=None):
        print("A is", a)
        print("B is", b)
        print("C is", c)



emp1 = Employee('John', 1, 1500)
emp2 = Employee('Mary', 2, 2000)

print(emp1.tax())
print(emp2.tax())

print(emp1.salaryPerDay())
print(emp2.salaryPerDay())


#Method overloading performed by calling the same method
#Hence, it is implicit
emp1.demo("a for emp1", "b for emp1")
emp2.demo()
emp2.demo("a for emp2", "b for emp2", "c for emp2")