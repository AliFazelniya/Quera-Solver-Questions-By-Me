# https://quera.org/problemset/303

def fibo(n, n1):

    print(n)
    
    if n > 1:

        fibo(n1 - n, n)


n = int(input())

n1 = int(input())

fibo(n, n1)
