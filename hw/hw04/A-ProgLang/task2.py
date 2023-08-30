#Write a script, which of the two entered
#numbers will determine which of them is
#more and which is less. Take into account
#the case of equality of numbers.

number_1 = int(input("Enter number 1:"))
number_2 = int(input("Enter number 2:"))

if number_1 > number_2:
  print(f"{number_1} is more {number_2}")
elif number_1 < number_2:
  print(f"{number_2} is more {number_1}")
else:
  print(f"{number_1} and {number_2} are equal")