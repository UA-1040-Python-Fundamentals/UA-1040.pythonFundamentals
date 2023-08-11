def number(st: str):
    lis = list(st)
    d = {}
    for i in set(lis):
        d[i] = lis.count(i)
    return d


def mein():
    print(number(input('Enter the string: ')))


if __name__ == '__main__':
    mein()
