def replaceQuotes(str):
    listOrigin = [ i for i in str ]
    listReplaceQuotes = []

    for symbol in listOrigin:
        if symbol == '\"':
            listReplaceQuotes.append('\'') 
        elif symbol == '\'':
            listReplaceQuotes.append('\"')
        else:
            listReplaceQuotes.append(symbol) 

    return ''.join(listReplaceQuotes)

print(replaceQuotes('spa\"m and spa\"m'))
print(replaceQuotes('spa\'m spa\'m'))
print(replaceQuotes('spam and spam'))
print(replaceQuotes('spa\"m spa\'m'))

input()