from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def generate(list, num, max):
    num *= 10
    if num >= max:
        return

    for next in [4, 7]:
        list.append(num + next) 
        generate(list, num + next, max)

def test():
    luckys = []
    generate(luckys, 0, 1000)

    num = int(input())

    for lucky in luckys:
        if num % lucky == 0:
            print('YES')
            return

    print('NO')

if __name__ == '__main__':
    test()