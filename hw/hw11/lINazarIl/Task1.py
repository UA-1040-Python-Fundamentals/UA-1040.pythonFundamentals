class NegativeAge(Exception):
    pas

def main():
    while True:
        try:
            age = int(input('Enter age: '))
            if age < 0:
                raise NegativeAge

            if age % 2:
                print('Age odd')
            else:
                print('Age even')
        except NegativeAge:
            print('Entered age are negative')

if __name__ == '__main__':
    main()