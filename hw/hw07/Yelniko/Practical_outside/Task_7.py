def solution(number):
    lis = [i for i in range(number) if i % 3 == 0 or i % 5 == 0]
    num = 0
    for i in lis:
        num += i
    return num
