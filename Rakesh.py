#qs1

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))

# print("sum is: ", a + b)

#qs2

# side = int(input("side of square is: "))

# print("area is: ", side ** 2)

#qs3

# a = float(input("enter the first number: "))
# b = float(input("enter the second number: "))

# print("avg is: ", (a + b) / 2)

#qs4

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))

# print(a >= b)

#qs5

# name = input("enter the name: ")

# print(len(name))

#qs6

# str = "$I am $ and i'm the $ symbol in python $$"

# print(str.count("$"))

#qs7

# nums = int(input("enter the number: "))

# if(nums % 2 == 0):
#     print("EVEN")

# else:
#     print("FALSE")

#qs8

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# c = int(input("enter the third number: "))

# if(a >= b and a >= c):
#     print("first number is greatest: ", a)
# elif(b >= c):
#     print("second number is greatest: ", b)

# else:
#     print("third number is greatest: ", c)

#qs9

# num = int(input("enter the number: "))

# if(num % 7 == 0):
#     print("multiple")

# else:
#     print("not multiple")

#qs10

# movies = []

# a = input("enter the movie name: ")
# movies.append(a)
# b = input("enter the movie name: ")
# movies.append(b)
# c = input("enter the movie name: ")
# movies.append(c)

# print(movies)

#qs11

# list = [1, 2, 1]

# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("it's palindrome")

# else:
#     print("not palindrome")

#qs12

# list = ("C", "D", "A", "A", "B", "B", "A")

# print(list.count("A"))

#qs13

# val = ["C", "D", "A", "A", "B", "B", "A"]
# val.sort()
# print(val)

#qs14

# dict = {
#     "table" : ("a piece of furniture", "list of facts & figure"), 
#     "cat" : "a small animal"
# }

# print(dict)

#qs15

# sub = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print("need of classroom: ",  len(sub))

#qs16

# marks = {}

# a = int(input("phy marks: "))
# marks.update({"phy": a})
# b = int(input("math marks: "))
# marks.update({"math": b})
# c = int(input("chem marks: "))
# marks.update({"chem": c})

# print(marks)

#qs17

# val = {
#     ("float", 9.0), ("int", 9)
# }
# print(val)

#qs18

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#qs19

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

#qs20

# n = int(input("enter the number: "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

#qs21

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

#qs22

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("founding idx: ", i)
#     i += 1

#qs23

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in nums:
#     print(i)

#qs24

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# i = 0

# for el in nums:
#     if(el == x):
#         print("founding idx: ", i)
#     i +=1

#qs25

# for i in range(1, 101):
#     print(i)

#qs26

# for i in range(100, 0, -1):
#     print(i)

#qs27

# n = int(input("enter the number: "))

# for i in range(1, 11):
#     print(n * i)

#qs28

# n = int(input("enter the number: "))
# sum = 0
# i = 0
# while(i <= n):
#     sum +=i
#     i +=1

# print("sum is: ", sum)

#qs29

# n = int(input("enter the number: "))
# fact = 1
# for i in range(1, n+1):
#     fact *=i 

# print("factorial is: ", fact)

#qs30

# cars = ["THAR", "MUSTANG", "LAMBORGINI", "BUGATTI", "JEEP"]

# def print_len(list):
#     print(len(list))

# print_len(cars)

#qs31

# cars = ["THAR", "MUSTANG", "LAMBORGINI", "BUGATTI", "JEEP"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cars)
# print()

#qs32

# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *=i
#     print(fact)

# calc_fact(4)

#qs33

# def converter(usd_val):
#     inr_val = usd_val * 83.91
#     print(usd_val, "USD =", inr_val, "INR")

# converter(100)

#qs34

# def founding(n):
#     if(n % 2 == 0):
#         print("EVEN")

#     else:
#         print("ODD")

# founding(6)

#qs35

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(6)
# print(sum)

#qs36

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# cars = ["THAR", "MUSTANG", "LAMBORGINI", "BUGATTI", "JEEP"]

# print_list(cars)

#example
