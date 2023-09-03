#Write a script that will check whether
#the entered number is even or odd and
#display the appropriate message.

number = int(input("Enter number:"))
print("The number is even" if number % 2 == 0 else "The number is odd")