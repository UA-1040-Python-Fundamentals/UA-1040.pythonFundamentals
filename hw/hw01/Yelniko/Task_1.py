inf = input('Enter the answers to the following questions, separated by commas sequentially.\n'
            '"WHAT IS YOUR NAME?"\n"HOW OLD ARE YOU?"\n"WHERE DO YOU LIVE?"\n').split(',')

if __name__ == '__main__':
    while True:
        try:
            print(f'"HELLO, {inf[0]}"\n"YOUR AGE IS {inf[1]}"\n"YOU LIVE IN {inf[2]}"')
            break
        except IndexError:
            print('You did not enter something, try again')
            inf = input().split(',')
