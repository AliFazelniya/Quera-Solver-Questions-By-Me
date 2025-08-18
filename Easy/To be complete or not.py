# https://quera.org/problemset/282

import math

n = int(input())

div_sum = 1

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        div_sum += i
        if i != n // i:
            div_sum += n // i
        
if n != 1 and div_sum == n:
    print("YES")
else:
    print("NO")
