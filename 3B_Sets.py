# https://contest.yandex.ru/contest/28964/problems/A/

nums1 = [int(n) for n in input().split()]
nums2 = [int(n) for n in input().split()]

print(len(nums1)+len(nums2)-len(set(nums1 + nums2)))


# https://contest.yandex.ru/contest/28964/problems/B/

nums = [int(x) for x in input().split()]
seen = set()

for n in nums:
    if n in seen:
        print('YES')
    else:
        print('NO')
        seen.add(n)

# https://contest.yandex.ru/contest/28964/problems/C/

nums = [int(x) for x in input().split()]
num_dict = {}
res = []

for n in nums:
    if n not in num_dict:
        num_dict[n] = 1
    else:
        num_dict[n] += 1
        
for n in num_dict:
    if num_dict[n] == 1:
        res.append(n)
        
print(*res, sep = ' ')


# https://contest.yandex.ru/contest/28964/problems/D/

Nmax = int(input())
possible = [2]*(Nmax+1)
the_end = False

def guess(nums, ans, possible):
    if ans == 'NO':
        for x in nums:
            possible[x] = 0
    elif ans == 'YES':
        for x in nums:
            possible[x] = 1
        for i in range(Nmax+1):
            if i not in nums and possible[i] == 1:
                possible[i] = 0
            
while not the_end:
    new_input = input()
    if str(new_input) == 'HELP':
        the_end = True
        break
    else:
        nums = [int(x) for x in new_input.split()]
        ans = str(input())
        guess(nums,ans,possible)
        
print(*[i for i in range(Nmax+1) if possible[i] == 1], sep = ' ')


# https://contest.yandex.ru/contest/28964/problems/E/

M = int(input())
witnesses = []
for i in range(M):
    witnesses.append(str(input()))
N = int(input())
plates = []
for i in range(N):
    plates.append(str(input()))
    
result = {}

def isWitnessOk(witness, plate):
    for symb in set(witness):
        if symb not in set(plate):
            return False
    return True

for i in range(len(plates)):
    for witness in witnesses:
        if isWitnessOk(witness,plates[i]):
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
                
if len(result) != 0:
    best = max(result.values())
    print(*[plates[k] for k, v in result.items() if v == best],sep='\n')
else:
    print(*plates, sep='\n')

