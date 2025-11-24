#ნომერი 1

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
x = float(input("enter a number "))

if x in num_list :
 print("the number is in list")
else :
 print("number is not in list")

#ნომერი 2

x = int(input("enter a number "))

if x%2 == 0:
 print("the number is even")
else :
 print("the number is odd")

#ნომერი 3
st1 = "nutsa"
st2 = "NuTsA"

if st1==st2:
 print("same object")
else:
 print("different object")

#ნომერი 4
num_list =[44, 23, 11, 8, 20, 56, 33, 55]
x = float(input("enter a number "))
if x > num_list[2] and x < num_list[-1]:
 print("More than list elements")
elif x==num_list[5]:
 print("equal")
else:
 print("None of the conditions were met")