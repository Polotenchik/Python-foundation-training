def splitFunc(str, splitter):
    listOrigin = [ i for i in str ]
    j = 0

    if splitter == '':
        return listOrigin
    else:
        list = []
        while j < (len(listOrigin)*2 - 1):
            if j % 2 == 0:
                list.append(str[j//2])
            else: 
                list.append(splitter)
            j = j + 1

        return list

print(splitFunc('spam', ''))
print(splitFunc('spam', '$'))
print(splitFunc('eggs', '_'))

input()