def can_reach_pump(distance_to_pump, fuel_left, miles_per_gallon):
    fuel_needed = distance_to_pump / miles_per_gallon
    return fuel_left >= fuel_needed

# Test examples
print(can_reach_pump(50, 2, 25))
print(can_reach_pump(100, 2, 25))
