# class Employee:
#     ID = 5
#     salary = 1000
#     department = "ABC"
#
#
# Steve = Employee()
#
# print(Steve.ID)
#
# #This is a new property and will only be added to Steve object
# Steve.title = "Manager"
# print(Steve.title)
#
# Carol = Employee()
#will throw error
#print(Carol.title)

#TODO: ASK if this is the case where we can add properties to the object
#on the fly, what is the point of having properties defined in the class
#when you don't know whether the objects will be having only those properties
#or some extra ones as well



class Employee:
    #Init is nothing but a constructor and self is similar to "this" in Java
    #We can also have default values --> that would make parameters optional
    #This is method overloading
    def __init__(self, ID = -1, salary = 0, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department


Steve = Employee(1, 5000, "HR")

print(Steve.department)
print(Steve.salary)
print(Steve.ID)

#Default constructor
Mark = Employee()
print(Mark.ID)
print(Mark.department)
print(Mark.salary)