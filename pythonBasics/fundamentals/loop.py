# CONDITIONAL STATEMENT=>

# age = int(input("enter age: "))
age = 21
age = 14
if age >= 18 :
    print("You can vote!")
else :
    print("YOu cant vote")

# clr = input("Enter colour R, Y, G: ")
# if clr == "R" :
#     print("Stop")
# elif clr == "Y":
#     print("Readyy!")
# elif clr == "G" :
#     print("Gooo")
# else :
#     print("enter from given letter")

if age>=18 :
    print("Adult")
elif age>=14 and age < 18 :
    print("Teenagerr")
else :
    print("child")

# even / odd

n = int(input("Enter num: "))

if n%2 == 0 :
    print("Even")
else :
    print("Odd")

# nested loop=

username = input("Enter name: ")
password = input("Enter pass: ")

if username=="admin" and password == "pass" :
    print("success")
else :
    if username!="admin" :
        print("wrong username") 
    else :
        print("wrong username") 
    
# match case: 

colour = input("Enter colour: ")

match colour:
    case "green":
        print("go")
    case "yellow":
        print("ready")
    case "red":
        print("stop")
    case _ :
        print("Wrong colour")

# loop

# while True :      #infinte
#     print("Hello world!")

n = 3
while n>=0 :
    print("num is", n)
    n-=1

# table for n

n = 5 
i=1
while i<=10 :
    if i==6 :
        continue
        i+=1
    print(n," * ",i," = ",n*i)
    i+=1
    if i==8 :
        break

print("outside...")

# forr

# in - membership operator : to check presence

string = "hello"

if 'o' in string:
    print("Existss")

print("outt..")

for var in string :
    print(var)


for i in range(5):  # [0 - n-1]
    print(i)
    print("Hello")


word = "artificial intelligence"
count = 0
for ch in word:
    if ch == 'i' :
        count += 1

print("count of i = ",i)

# vowels count 
cnt = 0
for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch =="o" or ch=="u" :
        cnt += 1

print("vowels count: ",cnt)


for i in range(5) :
    print(i)

for i in range(1,10) :
    print(i)

for i in range(1,10,2) :
    print(i)

sum = 0
for i in range(1,5+1) :
    sum += i

print(sum)


# FUNCTIONS

def fun():
    print("Helloooo")
    print("broo ")

fun()
fun()

def sum(a,b) :      #parameter
    return a+b

print(sum(4,8))    #argument
print(sum(8,3))

# avvgg

def cal_avg(a,b,c) :
    sum = a+b+c
    return sum/3

print(cal_avg(2,5,7))

# default fun

def add(a, b=9) :
    print(a+b)

add(5)
add(4,7)

# lambdaa

avg = lambda a,b : (a+b)/2
print(avg(4,5))

broo = 0
b2 = lambda broo : broo+1
print(b2)

# factorial

def fact(n) :
    f = 1
    for i in range (1, n+1) :
        f = f * i
    return f

print(fact(5))


# assignment

# 1 
salary = int(input("Enter your salary: "))
if salary < 30000 :
    tax = 5
    salary = salary - (salary * tax)/100
elif salary > 70000 :
    tax = 25
    salary = salary - (salary * tax)/100
else :
    tax = 15
    salary = salary - (salary * tax)/100

print(f"Your Salary after tax is {salary}")


# 2
a = int(input("Enter a integer: "))
b = int(input("Enter another integer: "))

print("Even num bet themm.. ")

if a%2 == 0 :
    for i in range(a+2,b,2) :
        print(i)
else :
    for i in  range(a+1,b,2) :
        print(i)


# 3
n = (input("Enter any digit: "))
print("Digits are : ")

for i in n :
    i = int (i)
    print(i%10)


# 4
n = (input("Enter any digit: "))
count = 0

for i in n :
    i = int (i)
    if i % 10 != 0 :
        count += 1

print(count)

# 5
n = (input("Enter any digit: "))
sum = 0

for i in n :
    i = int (i)
    m = i%10
    sum += m

print(sum)

# 6
for i in range(1,101,1) :
    if i % 3 == 0 or i % 5 == 0 :
        print(i)
    

# 7
n = input("Enter any integer or quit")
while (n != "quit") :
    n = int(n)
    if n > 0 :
        print(f"Positive {n}")
    else :
        print(f"Negative {n}")

    n = input("Enter any integer or quit")

# 8
def calc (a, b, opp) :
    if opp == '+' :
        return a+b
    elif opp == '-' :
        return a-b
    elif opp == '*' :
        return a*b
    elif opp == '/' :
        return a/b
    else :
        print("Wrong opperation ")

print(calc(5,9, '+'))

# 9 
def is_prime(n) :
    for i in range(2,n,1) :
        if n%i == 0:
            print("False")
            break
    else :
        print("True")

is_prime(7)

# 10 
n=56
m = int(input("Enter any numberr: "))

while m != 0 :
    if m > n :
        print("Guess is Too big")
        m = int(input("Enter any numberr: "))
    elif m < n :
        print("Guess is too small")
        m = int(input("Enter any numberr: "))
    elif m == n :
        print("Correct guess")
        m = int(input("Enter any numberr: "))