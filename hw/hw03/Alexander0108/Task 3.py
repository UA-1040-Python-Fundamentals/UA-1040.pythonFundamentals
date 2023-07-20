# # ЗАВДАННЯ 1

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

#Слова для детекції у тексті
words = ['better', 'never', 'is']

#Створення списку слів усього тексту та переведення їх у нижній регістр 
text_split = [b.lower() for b in (text.split())] 

#Цикл для фіксації необхідних слів та виведення на екран їх кількості
print ("ЗАВДАННЯ 1.1")
for i in set(text_split):
    if i in words:
        print(f"{i} - {text.count(i)}")
print()

print (f"ЗАВДАННЯ 1.2 \n{text.lower()}")

print(f"ЗАВДАННЯ 1.3 \n{text.replace('i', '&')}")

# ЗАВДАННЯ 2

number = 1324
print(f"\n Number = {number}")
print("\n ЗАВДАННЯ 2.1")
init = 1

number_str = str(number)

for answer in number_str:
    answer_int = int(answer)
    init *= answer_int

print(f"Product of the digits of this number: {init}")

print ("\n ЗАВДАННЯ 2.2")

print(f"Number in reverse order: {number_str[::-1]}")

print ("\n ЗАВДАННЯ 2.3")

digits = []

for dig in number_str:
    digits.append(int(dig))
    digits.sort()
    print(digits)


# ЗАВДАННЯ 3
print("\n ЗАВДАННЯ 3")

x = "This is x"
y = "This is y"

x, y = y, x
print(f"x → {x}\n and\ny → {y}")
