import math
count = 0
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

p = 5
q = 11
N = p*q

thigh = ((p-1) * (q-1))
print('thigh is ',thigh)

coprime_N = []
coprime_thigh = []
comprimes = []
#find co prime
for i in range(thigh):
    
        

    if coprime(i, N):
        coprime_N.append(i)

    if coprime(i, thigh):
        coprime_thigh.append(i)

for i in coprime_N:
    if i in coprime_thigh:
        comprimes.append(i)
comprimes.remove(1)
print('comprimes found are ',comprimes)

my_comprime = comprimes[0]

lock = [my_comprime, N]


# (d * my_comprime)%thigh == 1 where d is less then thigh

key = None
for i in range (100):

    ans = (my_comprime * i) % thigh
    if ans == 1:
        count += 1

    if count == 2:
        print('i is ',i, 'n*i is ',my_comprime*i)
        key = i
        break

print('lock is ',comprimes[0], N)
print('key is ', key, N)

print((2 ** 3) % 55)
print((8**67)%55)

