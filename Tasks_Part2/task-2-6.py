def splitByIndex(str, listIndexes):
    j = 0

    if len(listIndexes) == 0:
        return [ str ]
    else:
        list = []
        list.append(str[0:listIndexes[j]])

        while j < len(listIndexes):
            if j + 1 == len(listIndexes) or len(str) < listIndexes[j]:
                break
            list.append(str[listIndexes[j]:listIndexes[j + 1]])
            j = j + 1
        
        if len(str) > listIndexes[len(listIndexes) - 1]:
            list.append(str[listIndexes[len(listIndexes) - 1]:len(str)])

        return list

print(splitByIndex('spamandeggs', []))
print(splitByIndex('spamandeggs', [42]))
print(splitByIndex('spamandeggs', [4, 7]))
print(splitByIndex('Hello!MontyPython', [6, 11, 42]))

input()