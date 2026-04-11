
# # CLASSS ANDA OBJJ-

# # class Student :
# #     subject = "Python"
# #     college = "IIST"

# # stud1 = Student()
# # stud2 = Student()

# # print(stud1.college, stud1.subject)
# # print(stud2.college, stud2.subject)


# # CONSTRUCTORR AND TYPES-
#     # we cannot create multiple constructor in one class

# # class Student :
# #     def __init__(self) :      #default
# #         print("Constructor was called..")

# # std1 = Student()
# # std2 = Student()


# # class Student :
# #     def __init__(self, name, cgpa) :      #parametrized
# #         self.name = name
# #         self.cgpa = cgpa
    
# #     def get_cgpa(self) :
# #         return self.cgpa

# # std1 = Student("Rahul", 9.0)
# # std2 = Student("Lokesh", 9.2)

# # print(std1.name)
# # print(std2.name )

# # print(std1.get_cgpa())
# # print(std2.get_cgpa())


# # class Student :
# #     clg_name = "janta_clg"      #class attribute
# #     PI = 3.1

# #     def __init__(self, name, gpa, PI):
# #         self.name = name    #instance attribute
# #         self.gpa = gpa
# #         PI = 3.14

# # std1 = Student("Rahul", 9.2)

# # print(std1.name)
# # print(std1.PI)
# # print(Student.clg_name)


# # METHODS-

# # class Laptop :
# #     # class attribute
# #     storage_type = "ssd"

# #     # constructor
# #     def __init__(self, RAM, storage):
# #         self.RAM = self.RAM
# #         self.storage = storage

# #     # class method
# #     @classmethod
# #     def get_storage_type(cls):
# #         print(f"storage type {cls.storage_type}")
    
# #     # instance method
# #     def get_info(self) :
# #         print(f"laptop has {self.RAM} & {self.storage}")

# #     # static method
# #     @staticmethod
# #     def calc_discount(price, discount):
# #         final_price = price -  (discount * price / 100)
# #         print(f"discounted price = {final_price}")

# # l1 = Laptop("16gb", "512gb")
# # l2 = Laptop("8gb", "256gb")

# # l1.get_info()
# # Laptop.get_storage_type()
# # l1.get_storage_type()
# # l1.calc_discount(40_000, 10)

# # class Products :
# #     count = 0

# #     def __init__(self, name , price):
# #         self.name = name
# #         self.price = price
# #         count += 1

# #     @classmethod
# #     def get_count(cls) :
# #         print(f"product count is {cls.count}")

# #     def get_info(self) :
# #         print(f"price of {self.name} is {self.price} ")
    
# #     @staticmethod
# #     def calc_discount(price, discount):
# #         final_price = price -  (discount * price / 100)
# #         print(f"discounted price = {final_price}")
    
# # p1 = Products("phone", 10_000)
# # p2 = Products("lappy", 40_040)

# # p1.get_count()
# # p1.get_info()
# # p1.calc_discount(p1.price, 12)


# # # ENCAPSULATION -

# class BankAccount :
#     def __init__(self, name, balance):
#         self.name = name        #public
#         # self._balance = balance     #protected
#         self.__balance = balance    #private
    
#     def get_balance(self) :
#         return self.__balance

#     def set_balance(self, nbalance) :
#         self.__balance = nbalance


# # acc1 = BankAccount("Rahul", 1000)

# # print(acc1._balance)    #accesible why? - protected by conention not emforced only in python
# # print(acc1.name, acc1.get_balance())

# # acc1.set_balance(20_000)
# # print(acc1._BankAccount__balance)   #private can be access outside



# # INHERITANCE --

# class Employee :
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_end_time) :
#         self.end_time = new_end_time

# class Teacher (Employee) :
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff (Employee) :
#     def __init__(self, role):
#         self.role = role

# # t1 = Teacher("Maths")
# # t1.change_time("5pm")
# # print(t1.subject, t1.start_time, t1.end_time)

# # staff1 = AdminStaff("Manager")
# # print(staff1.role, staff1.start_time, staff1.end_time)


# # TYPESS --

# # 1) SINGLE LEVEL INHERITANCE

# # 2) MULTI LEVEL INHERITANCE
# class Employee :
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_end_time) :
#         self.end_time = new_end_time

# class AdminStaff (Employee) :
#     def __init__(self, role):
#         self.role = role

# class Accountant (AdminStaff) :
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary

# acc1 = Accountant(10_000, "CA")
# print(acc1.role, acc1.salary)


# # 3) MULTIPLE LEVEL INHERITANCE
# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class Student:
#     def __init__(self, gpa):
#         self.gpa = gpa

# class TA (Teacher, Student) :
#     def __init__(self, salary, gpa, name):
#         super().__init__(salary)
#         Student.__init__(self, gpa)
#         self.name = name

# ta1 = TA(10_000, 7.89, "Lokeshhh")
# print(ta1.name, ta1.salary, ta1.gpa)


# # ABSTRACTIONN

# from abc import ABC

# class Animal(ABC) :

#     # @abstractmethod
#     def make_sound(self):
#         pass

# class Lion (Animal) :
#     def make_sound(self):
#         print("Roar..")

# class Cow (Animal) :
#     def make_sound(self):
#         print("Moww..")

# lion = Lion()
# lion.make_sound()
# cow = Cow()
# cow.make_sound()


# # POLYMORPHISM -

# # function overloading
# class Employee :
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher (Employee) :
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# # DUCK TYPING-- no inheritance but same working
# class Teacher () :
#     def get_designation(self):
#         print("designation = Teacher")

# class Accountant() :
#     def get_designation(self):
#         print("designation = Accountant")

# t1 = Teacher()
# t1.get_designation()
# a1 = Accountant()
# a1.get_designation()


# # ASSIGNMENT --

# class BankAccount :
#     def __init__(self, account_num, owner_name, balance):
#         self.account_num = account_num
#         self.owner_name = owner_name
#         self._balance = balance

#     def deposit(self, deposite_amount) :
#         print(f"amount deposite is {deposite_amount}")
#         self._balance += deposite_amount
    
#     def withdraw(self, amount) :
#         if amount <= self._balance :
#             print(f"amount withdraw is {amount}")
#             self._balance -= amount
#         else :
#             print("Insufficient balance", self._balance)

#     def total_balance(self):
#         print(f"Balance is {self._balance}")

# acc1 = BankAccount(3987690, "babluu", 10_8678)
# acc2 = BankAccount(3987691, "tabluu", 18_678)

# acc1.deposit(2100)
# acc1.withdraw(700)
# acc1.total_balance()


# 2 book - title,author,list review,  new_rev, count_rev, dis_rev
# class Book :
#     def __init__(self, title, author, review):
#         self.title = title
#         self.author = author
#         self._review = review 

#     def new_review (self, add_rev) :
#         self._review.append(add_rev)
#         print("Thanks for Review")
    
#     def count_review(self) :
#         print("Number of reviews recieved: ",len(self._review))
    
#     def dis_review(self) :
#         for i in self._review :
#             print(i)

# b1 = Book("Chomuu", "Chaman gupta", ["4star", "5star", "1star", "2star"])
# b1.new_review("1star")
# b1.count_review()
# b1.dis_review()


# # 3 stud - _name, _roll, _mark  get&set

# class Student :
#     def __init__(self, name, roll, mark):
#         self._name = name
#         self._roll = roll
#         self._mark = mark

#     def get_name(self) :
#         return (self._name)

#     def get_roll(self) :
#         return (self._roll)

#     def get_mark(self) :
#         return (self._mark)

#     def set_name(self, new_name) :
#         if new_name != None : 
#             self._name = new_name
    
#     def set_roll(self, new_roll) :
#         if new_roll > 0 and new_roll <= 100 :
#             self._roll = new_roll
#         else :
#             print("Incorrect roll")
    
#     def set_mark(self, new_mark) :
#         if new_mark > 0 :
#             self._mark = new_mark
#         else :
#             print("marks can not be empty") 
    
# std1 = Student("chomuu", 85, 98)
# std2 = Student("Bhondu", 67, 33)

# print(std1.get_mark())
# std2.set_mark(89)
# print(std1.get_roll())
# print(std2.get_name())
