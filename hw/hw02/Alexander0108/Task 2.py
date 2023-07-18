print("Добрий день!\n"
       "Давайте порахуємо сумму, різницю, добуток, частку, "
       "цілочисельну частку, остачу від ділення та піднесення до степеня чисел 'a' та 'b'")

while True:
      while True:
         a = input("Введіть бажане число a: ")
         b = input("Введіть бажане число b: ")
         try:
              convert_a = int(a)
              convert_b = int(b)
              break
         except ValueError:
              print("У параметри необіхдно ввести числа.")
              continue
      def calc():
       print("І так, отримаємо:\n "
             f"a + b = {convert_a+convert_b}\n a - b = {convert_a-convert_b}\n "
             f"a * b = {convert_a*convert_b}\n a / b = {convert_a/convert_b}\n "
             f"a ^ b = {convert_a**convert_b}\n a // b = {convert_a//convert_b}\n "
             f"a % b = {convert_a%convert_b}")
      calc()
      agreement = input("Якщо потрібно ще щось порахувати напишіть 'так' в іншому випадку 'ні': ")
      if agreement == "так":
       print("Добре! Рахуймо далі!")
       continue
      else:
        break