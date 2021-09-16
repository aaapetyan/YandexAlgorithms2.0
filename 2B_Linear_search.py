# https://contest.yandex.ru/contest/28738/problems/A

def maxnumbers(seq):
    max_n = seq[0]
    ans = 0
    for number in seq:
        if number > max_n:
            max_n = number
            ans = 1
        elif number == max_n:
            ans += 1
    return ans

seq = []
n = -1
while n != 0:
    n = int(input())
    seq.append(n)
    
print(maxnumbers(seq))

# https://contest.yandex.ru/contest/28738/problems/B

seq = list(map(int, input().split()))

def mindist(house, shops):
    return min([abs(house-i) for i in shops])

def maxdist(seq):
    houses = []
    shops = []
    for i in range(len(seq)):
        if seq[i] == 1:
            houses.append(i)
        elif seq[i] == 2:
            shops.append(i)
    return max([mindist(house, shops) for house in houses])

print(maxdist(seq))

# https://contest.yandex.ru/contest/28738/problems/C

init_str = list(input())
count = 0
N = len(init_str)
for i in range(N//2):
    if init_str[i] != init_str[N-1-i]:
        count += 1
print(count)


# https://contest.yandex.ru/contest/28738/problems/D

L, K = map(int, input().split())
positions = list(map(int, input().split()))


def lavochki(L,K,positions):
    if L%2 == 1 and L//2 in positions:
        return [L//2]
    else:
        left = False
        right = False
        ind_l = L//2 - 1
        ind_r = L//2 + L%2

        while not left and ind_l >= 0:
            if ind_l in positions:
                left = True
            else:
                ind_l -=1
            
        while not right and ind_r <= L:
            if ind_r in positions:
                right = True
            else:
                ind_r += 1
            
        return ind_l, ind_r

print(*lavochki(L,K,positions),sep='\n')


# https://contest.yandex.ru/contest/28738/problems/E/

N = int(input())
diplomas = list(map(int, input().split()))
diplomas.remove(max(diplomas))
print(sum(diplomas))

