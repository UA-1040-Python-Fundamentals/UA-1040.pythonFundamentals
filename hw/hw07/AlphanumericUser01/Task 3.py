# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def chr_nmb(input_string):
    input_list = list(input_string)
    final_list = []

    for i in range(len(input_list)):
        final_list.append(input_list.count(input_list[i]))

    final_result = dict()
    for x in range(len(input_list)):
        final_result[input_list[x]] = final_list[x]

    return final_result


a = chr_nmb("hello")
print(a)
