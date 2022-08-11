from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())

if n % 2 == 0:
    o = n
    e = o 
else:
    o = n + 1
    e = n - 1
odd_sum = ((-2 -(o - 2)) * (o // 2))
even_sum = ((2 + e) * (e // 2))
print((odd_sum + even_sum) // 2)