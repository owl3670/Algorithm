def getPrimes():
    n = 10000
    primes = [True] * (n + 1)
    for i in range(2, n**0.5):
        for j in range(i + i, n, i):
            primes[j] = False
