from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

a = int(input())
b = int(input())
c = int(input())

li = []
li.append(a+b+c)
li.append(a+b*c)
li.append(a*b+c)
li.append(a*b*c)
li.append((a+b)*c)
li.append(a*(b+c))

print(max(li))