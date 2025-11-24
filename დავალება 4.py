# დავალება 1
text = input("enter a string: ")
utf8 = text.encode("utf-8") 
print("string in utf-8 is: ", utf8)

#დავალება 2
text = input("enter a string ")
text = text.strip().lower().replace("python", "Python")+ "python"

print(text)

# დავალება 3

text = input("enter a string ")
x = len(text) // 2

firsthalf = text[:x]

print("first half of your sentence is ", firsthalf)

# დავალება 4 
import string

text = input("enter a string: ")
letter = False
digit = False

for i in text:
    if i in string.ascii_letters:
        letter = True
    elif i in string.digits:
        digit = True
    else:
        print("the string is not valid")
        break
else:
    if letter and digit:
        print("the string is valid")
    else:
        print("the string is not valid")


#დავალება 5 

import base64
str = input("enter a string: ")
str16 = str.encode("utf-16")
str32 = str.encode("utf-32")
str64 = base64.b64encode(str.encode("utf-8"))

print(str16)
print(str32)
print(str64)

str16 = str16.decode("utf-16")
str32 = str32.decode("utf-32")
str64 = base64.b64decode(str64).decode("utf-8")

print(str16)
print(str32)
print(str64)
