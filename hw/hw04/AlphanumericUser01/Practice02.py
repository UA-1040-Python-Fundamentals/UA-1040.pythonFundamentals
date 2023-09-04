# Write a script that will check whether
# the entered number is even or odd and
# display the appropriate message.

a = int(input("Please enter a = "))
if a%2 == 0:
    print(f"""a is even""")
else:
    print(f"""a is odd""")