def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним числом")
    if age % 2 == 0:
        return "Парний вік"
    else:
        return "Непарний вік"

try:
    age = int(input("Введіть свій вік: "))
    result = check_age(age)
    print(result)
except ValueError as e:
    print(e)


