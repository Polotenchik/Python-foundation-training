def getLongtestWord(str):
    listWords = str.split(" ")
    longtestWord = listWords[0]
    j = 1

    while j < len(listWords):
        if len(listWords[j]) > len(longtestWord):
            longtestWord = listWords[j]
        j = j + 1

    return longtestWord

print(getLongtestWord('Python is simple and effective!'))
print(getLongtestWord('Any pythonista like namespaces a lot.'))
print(getLongtestWord('Monty Python'))

input()