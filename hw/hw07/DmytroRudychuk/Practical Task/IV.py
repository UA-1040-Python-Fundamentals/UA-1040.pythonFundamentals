# DESCRIPTION:
# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?



def str_to_int(word) -> int:
    int_str = int(word)
    return int_str

def is_int(word) -> int:
    if word.isdigit():
        int_str = int(word)
    return int_str

def str_list_to_int_list(str_list) -> list:
    int_list = list(map(int, str_list))
    return int_list


print(str_to_int("-996"))
print(is_int("45"))
print(str_list_to_int_list(["12", "-25", " 149"]))
