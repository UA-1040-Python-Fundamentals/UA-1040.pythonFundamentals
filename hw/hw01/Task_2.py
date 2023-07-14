while True:
    try:
        number = list(map(int, input('Enter numbers A and B separated by commas\n').split(',')))
        break
    except ValueError:
        print('You did not enter a number')

if __name__ == '__main__':
    print(f'A + B = {number[0]+number[1]}\nA - B = {number[0]-number[1]}\nA * B = {number[0]*number[1]}\n'
          f'A / B = {number[0]/number[1]}\nA**B = {number[0]**number[1]}\nA//B = {number[0]//number[1]}\n"'
          f'A%B = {number[0]%number[1]}\n')
