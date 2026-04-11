
# FILE OPERATION -
# DIFF MODES- 
# r - read
# w - overwrite 
# a - append
# x - create and open new file
# b - binary
# t - text
# + - open file for updation

# f = open("sample.txt", "r")     #file object

# data = f.read()
# data2 = f.readline()
# print(data, type(data))
# f.close()


# f = open("sample.txt", "w")     #file object

# f.write("Text to overwrite")
# print("Finished overwriting")
# f.close()


# f = open("sample.txt", "a")     #file object

# f.write("\nAdding new text using append")
# f.close()


# f = open("sample2.txt", "x")     #file object

# f.write("\nAdding new text using x")
# f.close()

# pointer at first index
# f = open("sample2.txt", "r+")     #file object

# f.write("a")
# print(f.read())
# f.close()

# pointer at last index
# f = open("sample2.txt", "a+")     #file object

# f.write("aa")
# print(f.read())
# f.close()


# pointer at first and overwrite
# f = open("sample2.txt", "w+")     #file object

# f.write("aa")
# print(f.read())
# f.close()


# # WITH KEYWORD --

# with open("sample.txt", "r") as f :
#     data = f.read()
#     print(len(data))

# # DELETE -
# import os
# os.remove("sample2.txt")


# WORD SEARCH AND PRINT LINE

# data = True
# line = 1
# word = "Python"
# with open("sample.txt", "r") as f:

#     while data :
#         data = f.readline()
#         if(word in data):
#             print(f"{word} found in line {line}")
#             break

#         print(data)
#         line += 1


# # EXCEPTION HANDELING-- 

# try :
#     x = 0
#     ans = 10/x

# except ZeroDivisionError :
#     print("Divide by zero is not allowed")

# except ValueError :
#     print("Can not enter other input then number")

# else:
#     print(f"ans is {ans}")
    
# finally :
#     print("Code performed...")


# # LIST COMPREHENSIONS--
# # # [output for item in iterable if condition]

# sqr = []
# for i in range(6) :
#     sqr.append(i*i)
# print(sqr)

# sqr = [i*i for i in range (6) if i%2 != 0]
# print(sqr)

# num = [-34, -66, -56, 85, 5, 6, -5]

# num = [0 if val < 0 else val for val in num]
# print(num)

# words = ["hello", "rgs", "frfvb"]

# words = [val.upper() for val in words]
# print(words)


# JSON MODE --

import json
# json.loads()      #json str -> py obj
# json.dumps()      #py obj -> json str

# json_str = '{"name" : "Pratham" , "isTeacher" : false}'
# py_obj = json.loads(json_str)

# print(type(json_str, py_obj))


# py_obj2 = {
#     "name" : "babbba",
#     "age" : 34,
#     "address" : "None"
# }

# json_str2 = json.dumps(py_obj2)

# print(type(json_str2), json_str2)


with open("data.json", "r") as f:

    py_obj = json.load(f)
    print(type(py_obj))


data = {
    "name" : "ffbg",
    "isblgk" : True
}
with open("data.json", "w") as f:

    json.dump(data , f, indent=4, sort_keys=True)
