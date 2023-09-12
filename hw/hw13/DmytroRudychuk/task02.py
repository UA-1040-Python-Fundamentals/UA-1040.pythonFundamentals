# Convert list containing miles to list containing kilometers (1 mile
# = 1.6 kilometers)
# a) using the map and some function
# b) using the map and lambda function

list_mile = [1, 2, 3, 4, 5, 7]


def to_km(num):
    result = num * 1.6
    return round(result, 1)

mile_map_list = list(map(to_km, list_mile))
lam = lambda x: round(x*1.6, 1)
lambda_list = [lam(x) for x in list_mile]

print(mile_map_list)
print(lambda_list)