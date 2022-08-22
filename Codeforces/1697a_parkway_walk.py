cnt = int(input())

for i in range(cnt):
    cases = list(map(int, input().split()))
    benches = list(map(int, input().split()))
    print(max(0, sum(benches) - cases[1]))