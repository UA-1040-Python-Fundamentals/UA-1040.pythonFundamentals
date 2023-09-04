pyton_philosophy = (f"""
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
Namespaces are one honking great idea -- let's do more of those!""")

# Find task
count_better = pyton_philosophy.count("better")
count_never = pyton_philosophy.count("never")
count_is = pyton_philosophy.count("is")
print("\nFind task:")
print("count_better =",count_better)
print("count_never =", count_never)
print("count_is =", count_is,"\n")

# Upper case task
print("Upper case task:", pyton_philosophy.upper(), "\n")

# Replace task
print("Replace task:", pyton_philosophy.replace("i", "&"))

