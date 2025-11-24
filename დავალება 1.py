#ნომერი 1
x = float(input("enter first number:"))
y = float(input("enter second number:"))
print (x+y, x-y, x*y, x/y, x//y, x%y, x**y)

#ნომერი 2
x = float(input("enter rhombus first diagonal length:"))
y = float(input("enter rhombus second diagonal length:"))

if x>0 and y>0:
 print("rhombus area is", x*y/2)


#ნომერი 3
x = float(input("enter meter"))

print(x, "is", x*100, "centimeter" )
print(x, "is", x*10, "decimeter" )
print(x, "is", x*1000, "milimeter" )
print(x, "is", x*0.006, "miles" )

#ნომერი 4
x = float(input("eneter triangles height"))
y = float(input("eneter triangles base"))

if x>0 and y>0:
 print("triangles area is ", x*y/2)

#ნომერი 5 
x = int(input("enter two digit number"))

if x>9 and x<100:
 print(x//10+x%10)

