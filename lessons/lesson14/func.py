def my_sort(l, key=None):

    for i in range(len(l)-1):
        for x in range(i+1, len(l)):
            e1 = l[i]
            e2 = l[x]
            if key:
                e1 = key(e1)
                e2 = key(e2)
            if e1 > e2:
                # l[i], l[x] = l[x], l[i]
                t = l[i]
                l[i] = l[x]
                l[x] = t
    return l
if __name__ == "__main__":
    l = [2, 5, 2, 7]

    my_sort(l)