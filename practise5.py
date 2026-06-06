# question>>1
# class Student:
#    def __init__(self,name, roll_no):
#     self.name = name  # Public attribute
#     self.roll_no = roll_no  # Public attribute
#     print(f"name is {self.name} and roll no is {self.roll_no}")
    
# obj = Student(name="shubh", roll_no=8)




# question>>2
# class Employee:
#     def __init__(self,name,salary):
#         # self.name = "sumit"
#         self.name = name  public
#         # self._salary = 50000  protected
#         self._salary = salary
        
# class Manager(Employee):
#     def display(self):
#         print(f" name is {self.name} & salry is {self._salary}")

# ob = Manager("rahul", 80000)
# ob.display()


# question>>3
# class BankAccount:
#     def __init__(self):
#         self.__balance = 45000       # private

#     def deposit(self,amount):
#         self.__balance = self.__balance + amount
    
#     def show_balance(self):
#         print(f"your current balance is {self.__balance}")
        
# obj3 = BankAccount()
# obj3.deposit(5000)
# obj3.show_balance()
# This will raise an error
# print(account.__balance)



# question>>4
# class Animal:
#     def __init__(self):
#         pass

#     def sound(self):
#         print("all animals can sound ")
        
# class Dog(Animal):
#     def sound(self):
#         print("it can bark")
        
# class Cat(Animal):
#     def sound(self):
#         print("it can meow")
        
# obj1 = Dog()
# obj1.sound()
# obj2 = Cat()
# obj2.sound()
        
        
        
# question>>4
# class Person:
#     def __init__(self, name):
#         self.name = name


# class Employee(Person):
#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id


# class Developer(Employee):
#     def __init__(self, name, employee_id, language):
#         super().__init__(name, employee_id)
#         self.language = language

#     def display(self):
#         print(f"Name is {self.name}")
#         print(f"Employee ID is {self.employee_id}")
#         print(f"Language is {self.language}")


# obj = Developer("mohit", "emp50", "python")
# obj.display()



# question>>5
# from abc import ABC , abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,length,breadth,unit):
#         self.length = length
#         self.breadth = breadth
#         self.unit = unit
#     def area(self):
#         a = self.length * self.breadth
#         print(f"{a} {self.unit}\u00B2")
     
# class Triangle(Shape):
#     def __init__(self,base,height,unit):
#         self.base = base
#         self.height = height
#         self.unit = unit
#     def area(self):
#         a = (self.base * self.height)/2
#         print(f"{a} {self.unit}\u00B2")
        
    
    
# r = Rectangle(13,12, "cm")
# r.area()
# t = Triangle(8,9,"m")
# t.area()

# for square we use \u00B2
# for cube we use \u00B3


# question>>7
# from abc import ABC, abstractmethod


# class LibraryItem(ABC):
#     def __init__(self, title):
#         self.title = title

#     @abstractmethod
#     def display_info(self):
#         pass


# class Book(LibraryItem):
#     def __init__(self, title, author, price):
#         super().__init__(title)
#         self.author = author
#         self.__price = price      # Private

#     def display_info(self):
#         print("Book Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.__price)
#         print("-" * 30)


# class Magazine(LibraryItem):
#     def __init__(self, title, issue_number):
#         super().__init__(title)
#         self.issue_number = issue_number

#     def display_info(self):
#         print("Magazine Title:", self.title)
#         print("Issue Number:", self.issue_number)
#         print("-" * 30)


# items = [
#     Book("Python Programming", "Guido", 500),
#     Magazine("Tech Today", 45)
# ]

# for item in items:
#     item.display_info()


# question>>8
# class BankAccount():
#     def __init__(self,balance):
#         self.__balance = balance
        
#      # getter method    
#     def get_balance(self):
#         print(f"current balance : {self.__balance}")
        
        
        
#     # setter method   
#     def set_balance(self, balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             print("Balance cannot be negative")
            
# obj = BankAccount(60000)
# obj.get_balance()
# obj.set_balance(90000)
# obj.get_balance()


# question>>9
# class Person:
#     def __init__(self,name):
#         self.name = name
    
# class Teacher(Person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject = subject
        
# obj = Teacher("rihan", "english")
# print(obj.name)
# print(obj.subject)



#question>>10
# class Vehicle:
#     def __init__(self):
#         pass
#     def start(self):
#         print("this vehicle is runnig")
        
# class Car(Vehicle):
#     pass 
    
# obj = Car()
# obj.start()



#question>>11
# class Camera:
#     def click_photo(self):
#         print("you have a camera to click photos")
        
# class Phone:
#     def calling(self):
#         print("you can call to anyone")

# class SmartPhone(Camera,Phone):
#     def __init__(self):
#         pass
    
# obj = SmartPhone()
# obj.click_photo()
# obj.calling()

#question>>12
# class Product:
#     def __init__(self,price):
#         self.__price = price
#     def get_price(self):
#         print(f"this is our current balance : {self.__price}")
#     def set_price(self,price):
#         if price >= 1:
#             self.__price = price
#         else:
#             print("your amount is invalid")
            
# obj = Product(8900)
# obj.get_price()
# obj.set_price(11000)
# obj.get_price()



#question>>13
# class Employee:
#     def work(self):
#         print("he can do anything ")
        
# class Developer(Employee):
#     def work(self):
#         super().work()
#         print("he can make websites & apps.")
        
# obj = Developer()
# obj.work()


#question>>14
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
     amount = int(input("enter your amount :"))
     print(f"Rs.{amount} has been debited from your account successfully via creditcard.")
    
class UPI(Payment):
    def pay(self):
     amount = int(input("enter your amount :"))
     print(f"Rs.{amount} has been debited from your account successfully via upi.")
    
obj = CreditCard()
obj.pay()
obj1 = UPI()
obj1.pay()
        
    
        
        

    
       
        
    
        
         
        
        


            
    