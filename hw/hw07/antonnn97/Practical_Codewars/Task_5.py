def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

input_string = "Hello world!"
reversed_result = reverse(input_string)
print(reversed_result)