# DESCRIPTION:
# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
#
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
#
# Example (Input --> Output)
#
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"

def reverse(st):
    new_st = st.split()
    my_list = list(reversed(new_st))
    return " ".join(my_list)


a = reverse("one no cares")
print(a)

# 'one no cares' should equal 'cares one no'