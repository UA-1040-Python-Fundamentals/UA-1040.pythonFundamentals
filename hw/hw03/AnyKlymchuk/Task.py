# Python Philosophy
python_philosophy = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Convert the entire Python philosophy text to lowercase
python_philosophy_lowercase = python_philosophy.lower()

# Find the number of occurrences of the words "better", "never", and "is" in the lowercase text
count_better = python_philosophy_lowercase.count("better")
count_never = python_philosophy_lowercase.count("never")
count_is = python_philosophy_lowercase.count("is")

# Replace all occurrences of the symbol "i" with "&" in the lowercase text
python_philosophy_modified = python_philosophy_lowercase.replace("i", "&")

# A four-digit natural number is specified
four_digit_number = 1234

# Find the product of the digits of this number
digits_product = 1
for digit in str(four_digit_number):
    digits_product *= int(digit)

# Write the number in reverse order
number_reversed = int(str(four_digit_number)[::-1])

# In ascending order, sort the numbers included in the given number
digits_sorted = sorted(int(digit) for digit in str(four_digit_number))

# Interchange the values of two variables without using the third variable
a, b = 10, 20
a, b = b, a

print("Occurrences of 'better':", count_better)
print("Occurrences of 'never':", count_never)
print("Occurrences of 'is':", count_is)

print("Python Philosophy with 'i' replaced by '&':\n", python_philosophy_modified)

print("Product of digits of the four-digit number:", digits_product)
print("Number in reverse order:", number_reversed)
print("Digits in ascending order:", digits_sorted)

print("Interchanged values: a =", a, "b =", b)
