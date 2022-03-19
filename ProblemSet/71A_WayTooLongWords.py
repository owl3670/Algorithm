num = int(input())

for i in range(num):
    str = input()
    if len(str) <= 10:
        print(str)
    else:
        print(f"{str[0]}{len(str) - 2}{str[-1]}")
