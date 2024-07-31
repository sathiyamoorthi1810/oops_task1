'''
1) Create a Student class with attributes like name, age, and marks. Include methods to display the student’s information.
'''

class Student:
    def __init__(self,name,age,marks):
        self.n = name
        self.a = age
        self.m = marks
    def display(self):
        print(f"Student name is:{self.n} \nStudent age is:{self.a}\nStudent Total marks is:{self.m}")

student1 = Student("sakthi",25,496)
student1.display()

'''
2) 'Create a base class Employee with attributes name and salary.
Derive a class Manager that adds the department attribute. 
Write a method in Manager to display all details.
'''
class Employee:
    def __init__(self,name,salary):
        self.n = name
        self.s = salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.d = department

    def display(self):
        print(f"Employee name is:{self.n}\nEmployee salary is:{self.s}\nEmployee department is:{self.d}")

emp1 = Manager("sakthi",250000,"developer")
emp1.display()

'''
3)Create two base classes Person and Employee, 
each with their own attributes and methods. 
Create a derived class Manager that inherits from both and displays details from both base classes.
'''

class Person:
    def __init__(self,name,age):
        self.n = name
        self.a = age
class Employee:
    def __init__(self,salary,role):
        self.s = salary
        self.r = role

class Manager(Person,Employee):
    def __init__(self,name,age,salary,role):
        Person.__init__(self,name,age)
        Employee.__init__(self,salary,role)
    def show_details(self):
        print(f"person name is:{self.n}\nperson age is:{self.a}\nEmployee salary is:{self.s}\nEmplyee role is:{self.r}")

manager = Manager("sathya",25,1500000,"developer")
manager.show_details()

'''
4) Implement a class Shape with a method area. 
Create subclasses Rectangle and Circle that override the area method to calculate areas of a rectangle and a circle, respectively.
'''
import  math
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.l = length
        self.w = width

    def area(self):
        return self.l*self.w

class Circle(Shape):
    def __init__(self,radius):
        self.r = radius

    def area(self):
        return math.pi*(self.r**2)

rect = Rectangle(10,5)
circle = Circle(5)
print(rect.area())
print(circle.area())

'''
5) Create a class BankAccount with private attributes balance and methods to deposit, withdraw, and check the balance.
'''
class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance

    def deoposit(self,amnt):
        self.__balance += amnt
        return self.__balance

    def withdraw(self,amnt):
        if amnt> self.__balance:
            print("Insufficient Balance")
        else:
            return self.__balance
    def check_bal(self):
        return self.__balance

cus1 = BankAccount(500)
print("deposit amnt is:",cus1.deoposit(1000))
print("withdrawn amnt is:",cus1.withdraw(500))
print("balance is:",cus1.check_bal())

''''
6)Create an abstract class Animal with an abstract method sound. 
Implement subclasses Dog and Cat with their specific implementations of the sound method.
'''
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog is barking")

class Cat(Animal):
    def sound(self):
        print("cat is meow")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()









