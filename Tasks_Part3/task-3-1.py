def generateNumbers(numb = 20):

    return { i: i**2 for i in range(1,numb + 1) }

print(generateNumbers())
print(generateNumbers(10))

input()