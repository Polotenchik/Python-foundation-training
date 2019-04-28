def getDigits(numb):
    listDigits = [ i for i in str(numb)]
    list = []
    j = 0

    while j < len(listDigits):
        list.append(int(listDigits[j]))
        j = j + 1

    return tuple(list)

print(getDigits(87178291199))
print(getDigits(1742))
print(getDigits(0))

input()