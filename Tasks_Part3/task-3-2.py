def countCharacters(str):
    list = [i for i in str]
    tpl = tuple(list)

    return { i: tpl.count(i) for i in str }

print(countCharacters('abcdefgabc'))
print(countCharacters('abc'))
print(countCharacters('abcccddadab'))

input()