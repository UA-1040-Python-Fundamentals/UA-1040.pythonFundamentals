def main():
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Where do you live? ")

    print("Hello, {}.".format(name))
    print("Your age is {}.".format(age))
    print("You live in {}.".format(city))

if __name__ == "__main__":
    main()
