import unittest

def get_primes():
    n = 10000
    isprimes = [True] * (n + 1)
    for i in range(2, int(n**0.5)):
        for j in range(i + i, n, i):
            isprimes[j] = False
    primes = []
    for idx, isprime in enumerate(isprimes):
        if idx == 0: continue
        if isprime:
            primes.append(idx)
    
    return primes

class Tests(unittest.TestCase):
    def test_get_primes(self):
        primes = get_primes()
        self.assertEqual(2, primes[1])
        self.assertEqual(3, primes[2])
        self.assertEqual(5, primes[3])
        self.assertEqual(29, primes[10])

if __name__ == '__main__':
    unittest.main()
