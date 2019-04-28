def getPairs(list):
    if len(list) < 2:
        return

    pairs = []
    j = 0

    while j < len(list):
        if j + 1 < len(list):
            listPairs = []
            listPairs.append(list[j])
            listPairs.append(list[j + 1])
            pairs.append(tuple(listPairs))
        j = j + 1

    return pairs

print(getPairs([1, 2, 3, 8, 9]))
print(getPairs(['need', 'to', 'sleep', 'more']))
print(getPairs([1]))

input()