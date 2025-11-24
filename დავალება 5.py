# დავალება 1
# my_list = []

# while True:
#     symbol = input("type 'a' to add number, type 'r' to remove number, type 'e' to exit ")

#     if symbol == 'a' :
#         n = int(input("enter a number to add "))
#         my_list.append(n)
#     elif symbol == 'r':
#         n = int(input("enter a number to remove "))
#         if n in my_list:
#             my_list.remove(n)
#         else:
#             print("the number is not in the list")
#     elif symbol == 'e':
#         print("the list is ", my_list)
#         exit()
        
# დავალება 2
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# print(my_list_1.index(210))
# my_list_1[-1].append("hello")
# my_list_1.remove(my_list_1[2])
# print(my_list_1)

# my_list_2 = my_list_1.copy()
# my_list_2.clear()

# print(my_list_2)
# print(my_list_1)

# დავალება 3
# import re
# phone_number =input("enter a phone number ")

# pattern = r"\(\d{3}\) \d{3}-\d{3}"

# if re.fullmatch(pattern, phone_number):
#     print(phone_number)
# else:
#     print("Invalid format")