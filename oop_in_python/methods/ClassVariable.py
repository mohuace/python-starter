from sympy.codegen.cnodes import static


class MyClass:
    name = "Daniel"


    #This is how you declare class methods. These belong to the class and you don't have to create
    #objects to access it. You cannot refer instance variables inside it as well.
    @classmethod
    def nameMethod(cls):
        print(cls.name)

    def instanceMethod(self):
        #Cannot ref name directly because it does not exist in this scope
        #Heve to use MyClass.name or self.name
        #print(name)
        print(self.name)


    #These are used as utility functions inside the class. No relation with
    #class or instance variables. Cannot be used to modify class variables or instance variables
    @staticmethod
    def staticMethod():
        print("This is a static method")
        MyClass.name = "Mohit"


class1 = MyClass()
class2 = MyClass()

#You can do this technically as python allows you to call class methods
#using instances of that class
class1.nameMethod()
class2.nameMethod()


MyClass.nameMethod()

#Cant do this
#MyClass.instanceMethod()

class1.instanceMethod()

class2.staticMethod()
MyClass.staticMethod()

MyClass.nameMethod()