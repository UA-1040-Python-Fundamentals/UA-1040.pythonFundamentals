# fullelement_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# float_list = [float(element) for element in fullelement_list]
#
# print(float_list)


def fibonacci_numbers(a):
    fibon1, fibon2 = 0, 1

    print(fibon1)
    print(fibon2)

    while fibon1 + fibon2 <= a:

        fibon_sum = fibon1 + fibon2

        print(fibon_sum)

        fibon1 = fibon2
        fibon2 = fibon_sum

a = int(input("Enter the numer of a: "))

fibonacci_numbers(a)
