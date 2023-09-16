def  MyFunc(age):
    if age < 18:
        raise ValueError("You are very young for a student")
    elif 18>=age<=44:
        return "You are a young student"
    elif 45 >= age <= 59:
        return "You are a middle student"
    elif age >= 60:
        raise ValueError("You are very old for a student.")

def search_for_chill(age):
    if age < 18:
        a = 18-age
        if a % 2 == 0:
            c ="age must be increased by an even number:"
        else:
            c = "it is necessary to increase the age by an odd number:"
    elif age > 60:
        a = 60 - age
        if a % 2 == 0:
            c ="age must be reduced by an even number:"
        else:
            c = "it is necessary to reduce the age by an odd number:"
    print(str(c) + str(abs(a)))
    return

try:
    age = int(input("Please enter your age: "))
    result = MyFunc(age)
    print(f"{result}")
except ValueError as error:
    print(f"Error: {error}")
    search_for_chill(age)




