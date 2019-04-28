import collections

def linearSeq(sequence):
    if isinstance(sequence, collections.Iterable):
        return [a for i in sequence for a in linearSeq(i)]
    else:
        return [sequence]

print(linearSeq([1, 2, 3, [ 4, 5, ( 6, 7 )]])) #[1,2,3,4,5,6,7]
print(linearSeq((1, 2, [3, 4], [ (5, 6), 7]))) #[1,2,3,4,5,6,7]

input()