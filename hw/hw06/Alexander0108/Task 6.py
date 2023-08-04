#Task 6.1

divis_2 = [num for num in range(10) if num %2 == 0]
odd_numb = [num for num in range(10) if num %2 == 1 and num %3 == 0]
not_divis = [num for num in range(10) if num %2 >= 1 and num %3 >= 1]
print(divis_2)
print(odd_numb)
print(not_divis)

#Task 6.2

dictionary = {'login': 'First'}
while True:
    login = str(input('Enter the login: '))
    if login == dictionary['login']:
        print('Welcome!')
        break
    else:
        print('Incorrect login. Please try again.')