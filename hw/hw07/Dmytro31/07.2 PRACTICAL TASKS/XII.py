def correct_tail(body, tail):
    return body[-1] == tail

animal_body = "fox"
animal_tail = "x"
result = correct_tail(animal_body, animal_tail)
print(result)