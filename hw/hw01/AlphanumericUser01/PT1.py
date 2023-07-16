# WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
#       “WHAT IS YOUR NAME?“
#        “HOW OLD ARE YOU?“
#        “WHERE DO YOU LIVE?“
# and will read the user's responses and display the corresponding messages:
#       “HELLO, (ANSWER(NAME))“.
#       “YOUR AGE IS  (ANSWER(AGE))“.
#       “YOU LIVE IN  (ANSWER(CITY))“.

NAME = str(input("WHAT IS YOUR NAME?\n"))
AGE = str(input("HOW OLD ARE YOU?\n"))
CITY = str(input("WHERE DO YOU LIVE?\n"))
print(f'HELLO, {NAME}\n'
      f'YOUR AGE IS {AGE}\n'
      f'YOU LIVE IN {CITY}\n'
      )
