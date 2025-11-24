# დავალება 1
# def my_func(arr1, arr2):
#  if len(arr1) == len(arr2):
#   list1 = list(zip(arr1, arr2))
#   list4 = []
#   for i in list1:
#     list4.append(str(i))
#   return list4
#  else:
#     print("Lists must be equal length.")


# list2 = [1, 2, 3]
# list3 = ['a', 'b', 'c']

# print(my_func(list2, list3))

#დავალება 2
# from functools import reduce

# arr1 = [1, 2, 3, 4, 5]

# try:
#     product = reduce(lambda x, y: x * y, arr1)
# except TypeError as ex:
#     print("Type mismatch")

# print(product)

# დავალება 3
# arr1 = [1, 2, 3, 4, 5, 6, 7]
# result = list(filter(lambda x: x % 2 == 1, arr1))
# print(result)


# დავალება 4
# arr1 = ['hello', 'world', 'coding', 'nod']
# def my_func(parameter1, parameter2='ing'):
#     arr2 = []  
#     try:
#         arr2 = list(filter(lambda word: word.endswith(parameter2), parameter1))
#     except TypeError as ex:
#         print("TypeError problem ")
#     except Exception as ex:
#         print(f" error: {ex}")
#     return arr2

# print(my_func(arr1))


