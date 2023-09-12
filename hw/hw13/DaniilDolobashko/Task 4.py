# simple function
def miles_to_kilometers(miles):
    return miles * 1.6

miles = [1.2, 5.8, 10, 7.1, 15]
km = list(map(miles_to_kilometers, miles))
print(km)

# lambda function
miles = [1.2, 5.8, 10, 7.1, 15]
km = list(map(lambda x: x * 1.6, miles))
print(km)