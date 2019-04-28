import collections
from functools import reduce

def linearSeq(sequence):
    if isinstance(sequence, collections.Iterable):
        return [a for i in sequence for a in linearSeq(i)]
    else:
        return [sequence]


def sumSeq(sequence):

    list = linearSeq(sequence)
    
    sum = reduce(lambda x,y: x + y, list)

    return sum

print(sumSeq([1, 2, 3, [ 4, 5, ( 6, 7 )]])) #[1,2,3,4,5,6,7]
print(sumSeq((1, 2, [3, 3], [ (5, 10), 7]))) #[1,2,3,4,5,6,7]

input()


