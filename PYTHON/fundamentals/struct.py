
# # String - we can not change a string : immmutable
# word = "pythonn"
# word2 = "sapolaa"

# print(len(word))

# print(word + " " + word2)

# for ch in word :
#     print(ch)


# # operationn--

# str = "hgbfjnkd"
# s = len(str)

# print(str[3])
# print(str[3:6]) #slicing
# print(str[3:])
# print(str[:])

# print(str[0 : -4])

# # formattingg

# a = 5
# b = 10
# sum = a+b

# print("Lang is {}".format("Pythonn"))
# print("Sum is {}".format(sum))

# print("sum of {} & {} is {}".format(a,b,sum))
# print("sum of {1} & {0} is {2}".format(a,b,sum))

# print("values of vars are {aa} & {bb}".format(aa=22, bb=55))

# # f strinng - use f and {}

# print(f"sum of {a} & {b} is {a+b}")

# # built in data typess -

# #LIST---
# m1 = [44,56,3,2,55,67,33,56]

# print(m1[5])
# print(len(m1))
# print(type(m1))

# m1[4] = "trr"
# print(m1[4])

# print( m1[0:4] )
# print( m1[ 4 : ])
# print( m1 [ 2 : -2])

# # METHODSS OF LISTT-      append, insert, sort, reverse

# nums = [3,5,6,4]

# nums.append(9)      #last
# print(nums)

# nums.insert(2 , 10)     # (index, var)
# print(nums)

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# # for in list
# x = 10
# idx = 0

# for val in nums :
#     if (val == x) :
#         print(f"{x} found at {idx}")
#         break
#     idx += 1

# # TUPPLES -- elements immutable

# tup = (2.45,6,8,37,4)
# print( tup[ : 3] )
# print(tup[4])
# # tup(6) = 10 // not possible

# tt = ( 55, 2, 4, 6)
# sum = 0

# for val in tt :
#     sum += val

# print(f"sum oftup {sum}")

# tt.index(2)     # 1 -- first occurance
# tt.count(5)     # 0 -- no of occurance


# # DICTIONARYY -- unordered key value pair

# info = {
#     "name" : "pratham",
#     "class" : 2,
#     "sub" : "python",
#     3.14 : "PI"
# }

# print( type(info))

# print( info["name"])
# print( info[3.14])

# info["class"] = 3
# print( info["class"])

# info["age"] = 6
# print(info["age"])

# # methods -- 

# print( info.keys())     #return all keys
# print( info.values())      #for all values

# print( info.items() )     #all key & values

# print( info.get('name') )    #returns value for the given key or none

# info.update( {"city": "Delhii"})  #to add new
# print(info.items())

# # SETSS -- unique element

# set = { 1,2,3,4,5,6,5,5}

# print(set)
# print(len(set))     #6

# set.add(9)
# print(set)

# # empty_set = set()

# #methodss

# s = { 1,2,4,5,6,6,}

# s.add(9)
# s.pop()     #remove random value
# s.remove(5)
# s.union(set)
# s.intersection(set)
# s.clear()

# # quess

# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "English"),
#     ("Tob", "English"),
#     ("Alice", "Math"),
# ]

# data =  { }
 
# for name,course in info :
#     if data.get(name) is None:
#         data[name] = set()
#     data[name].add(course)

# print(data)


# eng_list = []
# for name,course in info :
#     if course == "English" :
#         eng_list.append(name)

# # print(eng_list)


# sub_set = {"sub", }
# name_set = {"name",}
# for tup in info :
#     # print(tup[0])       #name
#     # print(tup[1])       #course
#     name_set.add(tup[0])
#     sub_set.add(tup[1])

# # print(name_set)
# # print(sub_set)

# # for name,course in info :
# #      print(name, course)



# # ASSIGNMENT -- 
# # PALINDROME-

# n = "madam"
# m = -1
# palindrome = "False"
# for ch in n :
#     if ch == n[m] :
#         m -= 1
#         palindrome = "True"
#     else :
#         break
# else :
#         palindrome = "False"      

# if palindrome == "True" :
#     print(f"it is not palindrome {n}")
# else :
#     print(f"It is palindrome {n}")


# # AVG OF NUM IN LIST
# li = [34,64,85,33,78]
# m = 0
# for i in li :
#     m = m + i
# print("Avg is : ",m/len(li))


# # TWO LIST INP MERGE SORT PRINT
# # l1 = int(input("Enter list: "))
# # l2 = int(input("Enter another list: "))
# l1 = [34,64,85,33,78]
# l2 = [65,63,67,22,56]

# merge = l1 + l2
# merge.sort()
# print(merge)


# # TUPLE OF EVEN ODD
# tup = (1,1,3,4,5,2,3)
# even = ()
# odd = ()

# for i in tup :
#     if i%2 == 0 :
#         even += (i,)
#     else :
#         odd += (i,)

# print(even)
# print(odd)


# dic = {
#     "loki" : 78,
#     "iron_man" : 99,
#     "batman" : 89
# }
# n = input("Enter your choice : ")
# while n != 0 :
#     if n == 'A' or n == 'a' :
#         # add
#         dic.update({"queen" : 99})
#         print("added new key")
#         print(dic.keys())
#         n = input("Enter your choice : ")

#     elif n == 'B' or n == 'b':
#         # update mark
#         dic["batman"]   = 79
#         print("marks updated for ",dic.get('batman'), dic['batman'])
#         n = input("Enter your choice : ")

#     elif n == 'C' or n == 'c' :
#         # search for stud
#         print("marks for queen: ",dic.get('queen'))
#         n = input("Enter your choice : ")

#     elif n == 'D' or n == 'd' :
#         # display all
#         print(dic.items())
#         n = input("Enter your choice : ")

#     else :
#         n = int(0)


# # list to dict
# li = ["apple", "bannana", "kiwi", "mango", "cherry"]
# words = {}

# for ch in li :
#     print(ch)
#     words.update({ ch : len(ch)})

# print(words.items())


# # inp str count _ 
# n = input("Enteer string : ")
# count = 0
# for ch in n :
#     if ch == ' ':
#         count += 1
# print(f"count is {count}")


# # commomn element in list:
# l1 = [2,4,1,7,4,8,0]
# l2 = [5,6,3,8,2,9,4,3,7] 
# l3 = []
# for i in l1 :
#     if i in l2 :
#         l3.append(i)
# print(l3)

# # common element in li :
# l1 = [5,6,3,8,2,9,4,3,7] 
# l2 = []
# for i in l1 :
#     if i not in l2:
#         l2.append(i)
#     else :
#         print(i)
# print(l2)

# # \\uniq char in str
# n = "gnbh jnkgbhfjbb kjnhbv"
# m = []
# count = 0
# for ch in n:
#     if ch not in m:
#         m.append(ch)
#         count += 1
#         print(ch)
# print(m, count)


# # PRACTICE SET -
# # list : mutable  = append , insert, sort, reverse
# # remove dup
# l1 = [1,2,2,3,4,4]
# n = len(l1)
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)

# print(l2)


# # 2nd large
# l = [10, 20, 4, 8, 9]
# large = 0
# for i in l :
#     if i > large :
#         second = large
#         large = i   #10 
#     elif i > second and i != large:
#         second = i

# print(second)


# # count of each
# lst = [1, 2, 2, 3, 1, 2]
# freq = {}
# for i in lst :
#     if i in freq:
#         freq[i] += 1
#     else :
#         freq[i] = 1

# print(freq)

# # tuple into list
# l1 = []
# tup = (1,2,2, 3,4, 5)
# for i in tup :
#     l1.append(i)

# print(l1)

# # find stud with max mark
# stud = {
#     "a" : 44, "b" : 67, "c" : 75, "d" : 33
# }

# large = 0
# for i in  stud :
#     if stud[i] > large :
#         large = stud[i]
#         topper = i

# print(large, i)


# # merge two dic
# d1 = {}
# d2 = { "a":4, "b":3}

# d1.update(d2)
# print(d1)


# # count char in str
# str = 'helloo'
# d ={}

# for ch in str :
#     if ch in d :
#         d[ch] += 1
#     else :
#         d[ch] = 1
# print(d)
