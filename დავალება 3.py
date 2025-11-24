# დავალება 1
n = int(input("enter a number:  "))
total = 0

for i in range(n): #თუ გვინდა რომ შეყვანილი რიცხვიც ჩაითვალოს მაშინ n+1 უნდა ეწეროს
  total +=i

print("the sum of numbers is", total)

#დავალება 2

n = int(input("enter a number "))

while n>0:
  print(n)
  n -= 1

# დავალება 3

num = 78
i = 1
print("A number has been chosen. Try to guess it: ")

while True:
     guess = int(eval(input(f"step #{i}. your guess: ")))
     if guess == num:
      print(f"you guessed a number. it was {num}.")
      break
     elif guess > num:
      print("too great")
     else:
       print("too less")

     i +=1
print ("game over")

# დავალება 4
total_sum = 0 

while True: 
  x = input("enter a number or write'sum' to calculate the sum: " ) 
  if x == "sum": 
   print("the sum of positive numbers is:", total_sum) 
   break  
  if x.isdigit(): 
   number = float(x) 
   if number > 0: 
     total_sum += number 





