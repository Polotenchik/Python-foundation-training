'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def getLPF(listFactors):
    j = len(listFactors)
    while j > 0:
        if isPrime(listFactors[j-1]):
            return listFactors[j-1]
        j = j - 1 

i = 1
n = 600851475143
list = []


while i*i <= n:
    if n%i == 0:
      list.append(i)
      if i != n//i:
        list.append(n//i)
    i = i + 1

list.sort()

print(getLPF(list)) #6857


input()
