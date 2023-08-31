#Convert boolean values to strings 'Yes' or 'No'.


def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

print(bool_to_word(False))
