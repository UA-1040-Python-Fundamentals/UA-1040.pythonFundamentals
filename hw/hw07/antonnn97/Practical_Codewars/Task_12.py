def correct_tail(body, tail):
    last_char = body[-1]

    if last_char == tail:
        return True
    else:
        return False

print(correct_tail("dog", "g"))
print(correct_tail("elephant", "t"))
print(correct_tail("zebra", "r"))