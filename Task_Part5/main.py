import collections

class OrderedSet(collections.abc.MutableSet):
    
    def __init__(self, iterable=None):
        self.items = []
        self.map = {}
        if iterable is not None:
            self |= iterable
    
    def __getitem__(self, index):
        return str(list(self)[index])

    def copy(self):
        return self.__class__(self)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def add(self, key):
        if key not in self.map:
            self.map[key] = len(self.items)
            self.items.append(key)
        return self.map[key]

    append = add

    def __contains__(self, key):
        return key in self.map

    def discard(self, key):
        if key in self:
            i = self.map[key]
            del self.items[i]
            del self.map[key]
            for k, v in self.map.items():
                if v >= i:
                    self.map[k] = v - 1

    def index(self, key):
        return self.map[key]

    def __str__(self):
        return "%s(%r)" % (self.__class__.__name__, sorted(list(self)))

l = OrderedSet(['z', 'a', 'z', 'b', 'c'])
print(l)
a = l[0]
l.add('test');
c = l.copy()
print('Copied ' + str(c))
print('Length is: ' + str(len(c)))
print(l.index('b'))
q = OrderedSet(['a', 'b', 'z'])
s = OrderedSet(['x', 'y', 'z'])

#l1 = OrderedSet([2, 1, 3, 7, 0])

print(l)
print(s)
print(q)

#Union sets
r = q | s
print('Union sets: ' + str(r))

#Intersection sets
r = q & s
print('Intersection sets: ' + str(r))

#Difference sets
r = q - s
print('Difference sets: ' + str(r))


print(a)
#print(l1)

input()