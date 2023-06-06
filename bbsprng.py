import math

def params_valid(p, q, s):
    return p != q and p % 4 == 3 and q % 4 == 3 and math.gcd(s, p*q) == 1

def count_runs(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            count += 1
    return count + 1

    
p = 191
q = 167
s = 599
n = p*q
l = 100

xis = []
zis = []
xis.append(pow(s, 2, n))

i = 1
while i <= l:
    xi = pow(xis[i - 1], 2, n)
    xis.append(xi)
    zis.append(xi % 2)
    i += 1
    
e = (l + 1) / 2
print(f"The generated numbers are:\n{zis}\nThe expected number of runs is: {e}.\nThe actual number of runs is: {count_runs(zis)}")