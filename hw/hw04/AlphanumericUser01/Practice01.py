# Write a script, which of the two entered
# numbers will determine which of them is
# more and which is less. Take into account
# the case of equality of numbers.

a = int(input("Please enter a = "))
b = int(input("Please enter b = "))

if a > b:
    print(f"""{a} is more than {b}""")
elif a < b:
    print(f"""{a} is les than {b}""")
elif a == b:
    print(f"""{a} is equal {b}""")