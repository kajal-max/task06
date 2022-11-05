# Question - 1

# test_str = "PyThoN"
# print("The original string is : " + str (test_str))
# result = [char for char in test_str if char.isupper()]
# print ("The uppercase characters in string are : " + str(result))


# Question - 2
# keys = ['Smit', 'Jaya', 'Rayyan']
# values = ['CSE', 'Networking', 'Operating System']
# mydict = dict(zip(keys,values))
# print(mydict)


# Question - 4
# s = "Consultadd Training"
# def reverse(s):
#     l = len(s) - 1
#     while l >= 0:
#         yield s[l]
#         l -= 1
# reverse_s = ''
# for i in reverse(s):
#     reverse_s += i
# print(reverse_s)


# Question - 5
# def  hello_decorator(func):
#     def inner1():
#         print("Hello , this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1
# def function_to_be_used():
#     print("This is inside the function !!")  
# function_to_be_used = hello_decorator(function_to_be_used) 
# function_to_be_used() 
 