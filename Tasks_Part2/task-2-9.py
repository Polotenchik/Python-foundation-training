def foo(list):
    multiplyAllElements = 1
    i = 0
    j = 0
    listProduct = []

    while i < len(list):
        multiplyAllElements = multiplyAllElements*list[i]
        i = i + 1

    while j < len(list):
        listProduct.append(int(multiplyAllElements/list[j]))
        j = j + 1

    return listProduct

print(foo([1, 2, 3, 4, 5])) #[120, 60, 40, 30, 24]
print(foo([3, 2, 1])) #[2, 3, 6]

input()