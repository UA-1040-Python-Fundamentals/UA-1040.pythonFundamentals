border = int(input("Enter a border: "))
i = 0
f = 1
text = "1"
while i < border:
    i = i + 1
    f = f * i
    text = text + " * " + str(i)
print(f"Factorial ({border}!) = {f}")
print(text, "=", f)
