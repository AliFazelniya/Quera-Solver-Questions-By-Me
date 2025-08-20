# https://quera.org/problemset/305

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

A = int(input())
B = int(input())

print(gcd(A, B))
