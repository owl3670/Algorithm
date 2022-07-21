from sys import stdin, stdout

input = stdin.readline
def print(obj):
    stdout.write(f'{str(obj)}\n')

num = int(input())

juices = list(map(int, input().split()))
juice_rate = 0
for juice in juices:
    juice_rate += juice / 100
print(juice_rate/num * 100)