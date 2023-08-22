# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep) -> int:
    """
    Returns the number of True occurrences in the array
    """
    c = 0
    for i in sheep:
        if i == True:
            c +=1
    return c




array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]
print(count_sheeps(array1))