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
possible = set(range(1, Nmax+1))
not_possible = set()

new_input = input().strip()
while new_input != 'HELP':
    nums = set(map(int, new_input.split()))
    ans = input().strip()
    if ans == 'NO':
        possible.difference_update(nums)
    elif ans == 'YES':
        possible.intersection_update(nums)
    new_input = input().strip()
print(*sorted(possible), sep=' ')


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

