# Ex1 - String 
# Enter text and display it one by one

# text = input("your text: ")
# for char in text:
#     print(char)

# Ex2 - String
# Enter text and display number of letter

# text = input("your text: ")
# print(len(text))

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter

# text = input("your text: ")
# isfound = False
# index = 0
# while index< len(text):
#     if text[index].isupper():
#         isfound = True
#     index += 1
# if isfound:
#    print("Yes")
# else:
#    print("No")
            
# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# text = input("your num: ")
# sum = 0
# letter = ""
# for i in range(len(text)):
#     if text[i] == " ":
#         letter += ""
#     else:
#         letter += text[i]
#         sum += int(text[i])
# print(letter)
# print("Total", sum)


# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 

# text = "454639"
# count_odd = 0
# count_even = 0
# for i in range(len(text)):
#     total = int(text[i])
#     if total % 2 == 0:
#         count_odd += 1
#     if total % 2 == 1:
#         count_even += 1
# print("Count of even :", count_even)
# print("Count of odd :", count_odd)
# print("sum all number:",count_even+count_odd)
# print("Reverse",text[::-1])

# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# num = int(input("your num: "))
# result = ""
# for i in range(num):
#     if num % 2 == 1:
#         result = "Odd"
#     else:
#         result = "Even"
# print(result) 

# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

# isfound_number = False
# while not isfound_number:
#     number = int(input("Enter number : "))
#     if number >= 10 and number <=20:
#         print("Continue")
#     else:
#         isfound_number = True
# print("Out of range")

# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
# text = "9394884039"
# number_eight = 0
# first_index_of_eight = 0
# isfound = False
# for i in range(len(text)):
#     if text[i] == "8":
#         number_eight += 1
#         if text[i] == "8" and not isfound:
#             first_index_of_eight = i
#         isfound = True
# print(number_eight)
# print(first_index_of_eight)

# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
# text = "3 4 5 6"
# no_space = ""
# total_x_two = 0
# for i in range(len(text)):
#     if text[i] != " ":
#         no_space += text[i] + " "
#         total_x_two += int(text[i]) * 2
#         print(total_x_two)
#     else:
#         no_space += ""
# print(no_space)


#Ex10 - Number
#Enter 5 numbers and find maximum and minimum value
#Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
# num1 = int(input("Enter a number: "))
# num_min = num1
# num_max = num1
# for i in range(4):
#     num = int(input("Enter a number:"))
#     if num > num_max:
#         num_max = num
#     if num < num_min:
#         num_min = num
# print("Max =", num_max)
# print("Min =", num_min)    
        

