#Task1
text='''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''


#Task1.1
print(text.count('better'))
print(text.count('never'))
print(text.count('is'))

#Task1.2
print(text.title())

#Task1.3
print(text.replace('i', '&'))

#Task2
natural_number=int(5267)

#Task2.1
mult = 1
while natural_number != 0:
    mult = mult * (natural_number % 10)
    natural_number = natural_number // 10
print(f'find the product of the digits of this number: {mult}.')

#Task2.2
natural_number=int(5267)
natural_number=str(natural_number)
rev=natural_number[::-1]
rev =int(rev)
print(f'write the number in reverse order: {rev}.')

#Task2.3
natural_number=int(5267)
n_list=list(str(natural_number))
n_list=sorted(n_list)
r="".join(n_list)
sort=int(r)
print(f'in ascending order, you need to sort the numbers included in the given number: {sort}.')

#Task3
a=52
b=67
a,b = b,a
print(f'Interchange the values of two variables without using the third variable.: variable a={a} and b={b}.')













