# დავალება 1
# int_list = [10,20,30,40]
# def my_func(n):
#     int_list.append(n)

# n = 90
# my_func(n)
# print(int_list)

   
# დავალება 2

# def my_func(num):
#     total = 0
#     for i in num:
#         total += i
#     return total

# list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# my_func(list)








# დავალება 3 
# gl_str = "Global"
# def my_func():
#     gl_str = "nutsa"
#     return gl_str




# დავალება 4

# def my_func(number):
#     if number == 0:
#         return 0
#     return number % 10 + my_func(number // 10)
    

#  დავალება 5

# def my_func(str):
#  if len(str) == 0:
#   return ""
#  return str[-1] + my_func(str[:-1])


# ლექციის დროს მოცემული დავალება
# def flatten(arg):
#     for item in arg:
#       if isinstance(item, (list, tuple, set, frozenset)):
#         yield from flatten(item)
#       elif isinstance(item, dict):
#         yield from flatten(item.values())
        
       
#       else:
#        yield item 


# arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': '256'}, (8, [9, 0], True, {5, 8, False})]

# arr = list(flatten(arr))
# print(arr)