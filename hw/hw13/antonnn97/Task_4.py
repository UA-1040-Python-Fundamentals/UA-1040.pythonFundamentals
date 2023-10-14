miles = [10, 20, 30, 40, 50]

def miles_to_kilometers(mile):
    return mile * 1.6

kilometers = list(map(miles_to_kilometers, miles))
print(kilometers)

kilometers2 = list(map(lambda mile: mile * 1.6, miles))
print(kilometers2)