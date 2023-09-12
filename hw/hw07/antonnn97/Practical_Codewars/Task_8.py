def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left

    if max_distance >= distance_to_pump:
        return True
    else:
        return False

print((zero_fuel(50, 25, 2)))
print((zero_fuel(100, 50, 1)))
