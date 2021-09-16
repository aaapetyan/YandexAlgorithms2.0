# https://contest.yandex.ru/contest/28730/problems/A

def module(r,i,c):
    ind = {0: 3, 1: c, 2: 2, 3: 3, 4: 3, 5: 5, 6: 0, 7: 1}
    if r == 0:
        if i == 0:
            return c
        elif i == 4:
            return 4
        else:
        	return ind[i]
    else:
        return ind[i]
        
r = int(input())
i = int(input())
c = int(input())

print(module(r,i,c))

# https://contest.yandex.ru/contest/28730/problems/B/

input_line = input()
N = int(input_line.split()[0])
n1 = int(input_line.split()[1])
n2 = int(input_line.split()[2])

print(min(abs(n1-n2)-1,N-abs(n1-n2)-1))

# https://contest.yandex.ru/contest/28730/problems/C/

date = input()
x = int(date.split()[0])
y = int(date.split()[1])

if x > 12 or y > 12:
    print(1)
elif x == y:
    print(1)
else:
    print(0)
    
# https://contest.yandex.ru/contest/28730/problems/D/

N = int(input())
seq = list(map(int, input().split()))

if N%2 == 1:
    print(seq[N//2])
else:
    print((seq[N//2-1]+seq[N//2])//2)
    
# https://contest.yandex.ru/contest/28730/problems/E/

d = int(input())
coords = input()
x = int(coords.split()[0])
y = int(coords.split()[1])

if x < 0:
    if y <= d/2:
        print(1)
    else:
        print(3)
elif x == 0:
    if y < 0:
        print(1)
    elif 0 <= y <= d:
        print(0)
    else:
        print(3)
else:
    if y < 0:
        if x <= d/2:
            print(1)
        else:
            print(2)
    elif y > d:
        if x <= d/2:
            print(3)
        else:
            print(2)
    else:
        if x <= d - y:
            print(0)
        else:
            if x >= d/2 or x == y:
                print(2)
            else:
                print(3)

