
# PRINT- fun jo output deta hai screen par

print("Hello World!", "\nHii")

# identifier
name = "pratham"
age = 19
isPrime = None

print("my name is: ", name, age)

print(type(name))
print(type(age))

# Datatype =
# Integer
# Float
# String 
# boolean 
# None

# LOGICAL --
# not
# and
# or

print(not(5>8))
print((5>0) and (3>2))
print((7>9) or (8<9))

# TYPE Casting--

ans1 = int (5 - 2.0)
ans2 = 6 + 8.0
print(ans1, type(ans1))
print(ans2, type(ans2))

name = input("enter name: ")
print(name)

a = int(input("Enter value1: "))
b = int(input("Enter value2: "))

print(a+b)


# /ASSIGNMENT =>1
# 1
name = input("enter name: ")
age = int(input("enter age: "))

print("Hello ",name ,"you are ",age ,"years old!")

# 2
a = int(input("Enter v1: "))
b = int(input("Enter v2: "))

print("sum =",a+b)
print("diff =",a-b)
print("divi =",a/b)
print("rem =", a%b)

# 3
a1 = int(input("enter a1: "))
a2 = int(input("enter a2: "))
a3 = float(input("enter a3: "))

sum = float(a1+a2+a3)
print("avg ",sum/3.0)

# 4
num = input("enter num: ")
int(num)
print(num, type(num))
float(num)
print(num, type(num))
str(num)
print(num, type(num))

# 5
x = 10 + 3 * 2 ** 2    #22

# 6
a1 = int(input("enter a1: "))
a2 = int(input("enter a2: "))
a3 = a2
a2 = a1
a1 = a3

# 7
temp = float(input("Enter temp celsius: "))
Ftemp = (temp * (9/5)) + 32
print(Ftemp)

# 8
r = float(input("Enter radius: "))
area = 3.14*r*r
print(area)

# 9
pr = float(input("enter pr: "))
rr = float(input("enter rr: "))
tt = float(input("enter tt: "))
print("si =", (pr*rr*tt)/100)

# 10
inp = 45.78
print("decimal part",int(inp))
print("fract part", (inp - int(inp)))