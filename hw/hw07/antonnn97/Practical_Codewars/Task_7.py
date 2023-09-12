def solution(number):
    list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
    return sum(list)

print(solution(7))