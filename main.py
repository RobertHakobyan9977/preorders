def S(i, K, n):
    return 1 + sum(0 if len(set(j & k for k in K) - K) - 1 else S(j + 1, K | {j | k for k in K}, n) for j in range(i, 2**n))

N = int(input('Enter number: '))

result = [S(1, {0, 2**n - 1}, n) for n in range(0, N+1)]

print(result)